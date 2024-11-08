from src.decorators.observer import observer_class, observer
from src.constants.observers import Observers
from src.utils.valid_input import input_string, input_phone, input_email, input_number


@observer_class
class View:
    def __init__(self, model):
        self.__model__ = model

    @staticmethod
    def clear():
        print("\033[H\033[J", end="")

    @staticmethod
    def render(*args):
        print(*args)

    # Input

    @staticmethod
    def add_contact():
        name = input_string("Enter name: ")
        phone = input_phone("Enter phone: ")

        return name, phone

    @staticmethod
    def change_contact():
        name = input_string("Enter name: ")
        phone = input_phone(f'Enter new phone for "${name}": ')

        return name, phone

    @staticmethod
    def show_phone():
        name = input_string("Enter name of contact: ")

        return name

    @staticmethod
    def show_all_contacts():
        pass

    @staticmethod
    def add_birthday():
        name = input_string("Enter name of contact for which you want add birthday: ")
        birthday = input_string(f'Enter birthday for ${name}: ')

        return name, birthday

    @staticmethod
    def show_birthday():
        name = input_string("Enter name: ")

        return name

    @staticmethod
    def add_email():
        name = input_string("Enter name: ")
        email = input_email("Enter email: ")

        return name, email

    @staticmethod
    def add_address():
        name = input("Enter name: ")
        address = input("Enter address: ")

        return name, address

    @staticmethod
    def show_birthdays_in_days():
        days = input_number("Enter number of days from now to show birthdays: ")

        return days

    @staticmethod
    def change_name():
        old_name = input_string("Enter old name: ")
        new_name = input_string("Enter new name: ")

        return old_name, new_name

    @staticmethod
    def delete_contact():
        name = input_string("Enter name of contact to delete: ")

        return name

    @staticmethod
    def add_notes():
        name = input_string("Enter name of contact o add notes: ")
        number_of_notes = input_number("How much notes you want to add (number): ")
        notes = []

        for i in range(number_of_notes):
            note = input_string(f"Enter note #{i+1}")
            notes.append(note)

        return name, ', '.join(notes)

    @staticmethod
    def show_notes():
        name = input_string("Enter name: ")

        return name

    @staticmethod
    def delete_note():
        name = input_string("Enter name of contact: ")
        index = input_number("Enter index to delete note: ")

        return name, index

    @staticmethod
    def edit_note():
        name = input_string("Enter name of contact: ")
        index = input_number("Enter index of note: ")
        new_note = input_string("Enter text of new note: ")

        return name, index, new_note



    # Output

    @observer(Observers.EditNote)
    def edit_note_result(self, **kwargs):
        index, name = kwargs.get('result')

        self.render(f"Note {index} for {name} updated.")

    @observer(Observers.DeleteNote)
    def delete_note_result(self, **kwargs):
        index, name = kwargs.get('result')

        self.render(f"Note {index} for {name} deleted.")

    @observer(Observers.ShowPhone)
    def show_phone_result(self, **kwargs):
        name, = kwargs.get('args')
        phones = kwargs.get('result')

        self.render('phone:', name, ", ".join(phone.value for phone in phones))

    @observer(Observers.AddContact)
    def add_contact_result(self, **kwargs):
        self.render("Contact added")

    @observer(Observers.ShowAllContacts)
    def show_all_contacts_result(self, **kwargs):
        contacts = kwargs.get('result')

        if contacts is None:
            self.render('No contacts')
            return
        self.render("\n".join([f"{name}: {', '.join(phones)}" for name, phones in contacts.items()]))

    def change_contact_name(self):
        old_name = input_string("Enter old name: ")
        new_name = input_string("Enter new name: ")

        return old_name, new_name

    @observer(Observers.ChangeContactName)
    def change_contact_name_result(self, **kwargs):
        old_name, new_name = kwargs.get('args')
        new_name = kwargs.get('result')

        self.render(f"Contact '{old_name}' has been changed to '{new_name}'")

    def change_contact_phone(self):
        name = input_string("Enter contact name: ")
        old_phone = input_phone("Enter old phone: ")
        new_phone = input_phone("Enter new phone: ")

        return name, old_phone, new_phone

    @observer(Observers.ChangeContactPhone)
    def change_contact_phone_result(self, **kwargs):
        name, old_phone, new_phone = kwargs.get('result')

        self.render(f"You changed phone for contact '{name}' from {old_phone} to {new_phone}")

    @observer(Observers.AddBirthday)
    def add_birthday_result(self, **kwargs):
        name, birthday = kwargs.get('result')
        self.render(f"Birthday for {name} set to {birthday}.")

    @observer(Observers.ShowBirthday)
    def show_birthday_result(self, **kwargs):
        name, birthday = kwargs.get('result')
        self.render(f"{name}'s birthday is on {birthday.strftime('%d.%m.%Y')}" if birthday else f"{name} has no birthday recorded.")

    @observer(Observers.AddEmail)
    def add_email_result(self, **kwargs):
        name, email = kwargs.get('result')
        self.render(f"Email '{email}' for {name} added.")

    @observer(Observers.AddAddress)
    def add_address_result(self, **kwargs):
        name, address = kwargs.get('result')

        self.render(f"Address for {name} added. Address: {address}")

    @observer(Observers.ShowBirthdaysInDays)
    def show_birthdays_in_days_result(self, **kwargs):
        days, = kwargs.get('args')
        contacts = kwargs.get('result')
        if not contacts:
            self.render(f"No contacts with birthdays in {days} days.")
        self.render(f"Contacts with birthdays in {days} days: " + ", ".join(contacts))

    @observer(Observers.DeleteContact)
    def delete_contact_result(self, **kwargs):
        name = kwargs.get('args')
        result = kwargs.get('result')

        if result is True:
            self.render(f"Contact with name '{name}' has been deleted")
        else:
            self.render(f"Contact not found")

    @observer(Observers.AddNotes)
    def add_notes_result(self, **kwargs):
        name = kwargs.get('result')

        self.render(f"Notes for {name} added.")

    @observer(Observers.ShowNotes)
    def show_notes_result(self, **kwargs):
        name, notes = kwargs.get('result')

        self.render(f"{name}'s notes:\n{notes}" if notes else f"{name} has no notes recorded.")
