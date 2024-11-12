from src.decorators.observer import observer_class, observer  # Імпортує декоратори для реалізації патерну "спостерігач"
from src.constants.observers import Observers  # Імпортує константи, що визначають типи сповіщень для спостерігачів
from src.utils.valid_input import input_string, input_phone, input_email, input_number  # Імпортує функції для введення та валідації даних

@observer_class
class View:
    # Ініціалізує представлення з моделлю даних
    def __init__(self, model):
        self.__model__ = model

    @staticmethod
    def clear():
        # Очищує консоль
        print("\033[H\033[J", end="")

    @staticmethod
    def render(*args):
        # Відображає передані аргументи у вигляді тексту
        print(*args)

    # Методи введення даних

    @staticmethod
    def search_notes_by_tag():
        # Запитує тег для пошуку нотаток
        tag = input_string("Enter tag to search notes: ")
        return tag

    @staticmethod
    def add_contact():
        # Запитує ім'я та телефон для нового контакту
        name = input_string("Enter name: ")
        phone = input_phone("Enter phone: ")

        return name, phone

    @staticmethod
    def change_contact():
        # Запитує ім'я контакту і новий номер телефону для зміни
        name = input_string("Enter name: ")
        phone = input_phone(f'Enter new phone for "{name}": ')

        return name, phone

    @staticmethod
    def show_phone():
        # Запитує ім'я контакту для показу номеру телефону
        name = input_string("Enter name of contact: ")

        return name

    @staticmethod
    def show_all_contacts():
        # Показує всі контакти (поки що реалізація відсутня)
        pass

    @staticmethod
    def add_birthday():
        # Запитує ім'я контакту та додає дату народження
        name = input_string("Enter name of contact for which you want add birthday: ")
        birthday = input_string(f'Enter birthday for "{name}": ')

        return name, birthday

    @staticmethod
    def show_birthday():
        # Запитує ім'я контакту для показу дня народження
        name = input_string("Enter name: ")

        return name

    @staticmethod
    def add_email():
        # Запитує ім'я та електронну адресу контакту
        name = input_string("Enter name: ")
        email = input_email("Enter email: ")

        return name, email

    @staticmethod
    def add_address():
        # Запитує ім'я та адресу контакту
        name = input("Enter name: ")
        address = input("Enter address: ")

        return name, address

    @staticmethod
    def show_birthdays_in_days():
        # Запитує кількість днів, щоб показати дні народження в межах цього періоду
        days = input_number("Enter number of days from now to show birthdays: ")

        return days

    @staticmethod
    def change_name():
        # Запитує старе та нове ім'я для зміни контакту
        old_name = input_string("Enter old name: ")
        new_name = input_string("Enter new name: ")

        return old_name, new_name

    @staticmethod
    def delete_contact():
        # Запитує ім'я контакту для видалення
        name = input_string("Enter name of contact to delete: ")

        return name

    @staticmethod
    def add_notes():
        # Запитує ім'я контакту та додає нотатки
        name = input_string("Enter name of contact to add notes: ")
        notes = []
        note = input_string(f"Enter note: ")
        notes.append(note)

        return name, ', '.join(notes)

    @staticmethod
    def show_notes():
        # Запитує ім'я контакту для показу нотаток
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
    # Методи виведення даних

    @observer(Observers.ShowTags)
    def search_notes_by_tag_result(self, **kwargs):
        # Відображає результати пошуку нотаток за тегом
        tag = kwargs.get('args')[0] if kwargs.get('args') else None
        notes = kwargs.get('result')
        if not notes:
            self.render(f"No notes found with tag '{tag}'.")
        else:
            self.render(f"Notes with tag '{tag}':" + "".join(notes))

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
        # Відображає телефонні номери для вказаного контакту
        name, = kwargs.get('args')
        phones = kwargs.get('result')

        self.render('phone:', name, ", ".join(phone.value for phone in phones))

    @observer(Observers.AddContact)
    def add_contact_result(self, **kwargs):
        # Відображає повідомлення після додавання контакту
        self.render("Contact added")

    @observer(Observers.ShowAllContacts)
    def show_all_contacts_result(self, **kwargs):
        # Відображає всі контакти
        contacts = kwargs.get('result')

        if contacts is None:
            self.render('No contacts')
            return
        self.render("\n".join([f"{name}: {', '.join(phones)}" for name, phones in contacts.items()]))

    def change_contact_name(self):
        # Запитує старе та нове ім'я для зміни контакту
        old_name = input_string("Enter old name: ")
        new_name = input_string("Enter new name: ")

        return old_name, new_name

    @observer(Observers.ChangeContactName)
    def change_contact_name_result(self, **kwargs):
        # Відображає результат зміни імені контакту
        old_name, new_name = kwargs.get('args')
        new_name = kwargs.get('result')

        self.render(f"Contact '{old_name}' has been changed to '{new_name}'")

    def change_contact_phone(self):
        # Запитує ім'я контакту, старий та новий номер телефону
        name = input_string("Enter contact name: ")
        old_phone = input_phone("Enter old phone: ")
        new_phone = input_phone("Enter new phone: ")

        return name, old_phone, new_phone

    @observer(Observers.ChangeContactPhone)
    def change_contact_phone_result(self, **kwargs):
        # Відображає результат зміни номера телефону контакту
        name, old_phone, new_phone = kwargs.get('result')

        self.render(f"You changed phone for contact '{name}' from {old_phone} to {new_phone}")

    @observer(Observers.AddBirthday)
    def add_birthday_result(self, **kwargs):
        # Відображає результат додавання дати народження
        name, birthday = kwargs.get('result')
        self.render(f"Birthday for {name} set to {birthday}.")

    @observer(Observers.ShowBirthday)
    def show_birthday_result(self, **kwargs):
        # Відображає дату народження контакту
        name, birthday = kwargs.get('result')
        self.render(f"{name}'s birthday is on {birthday.strftime('%d.%m.%Y')}" if birthday else f"{name} has no birthday recorded.")

    @observer(Observers.AddEmail)
    def add_email_result(self, **kwargs):
        # Відображає результат додавання електронної адреси
        name, email = kwargs.get('result')
        self.render(f"Email '{email}' for {name} added.")

    @observer(Observers.AddAddress)
    def add_address_result(self, **kwargs):
        # Відображає результат додавання адреси
        name, address = kwargs.get('result')

        self.render(f"Address for {name} added. Address: {address}")

    @observer(Observers.ShowBirthdaysInDays)
    def show_birthdays_in_days_result(self, **kwargs):
        # Відображає контакти, які мають дні народжень у зазначений період
        days, = kwargs.get('args')
        contacts = kwargs.get('result')
        if not contacts:
            self.render(f"No contacts with birthdays in {days} days.")
        self.render(f"Contacts with birthdays in {days} days: " + ", ".join(contacts))

    @observer(Observers.DeleteContact)
    def delete_contact_result(self, **kwargs):
        # Відображає результат видалення контакту
        name = kwargs.get('args')
        result = kwargs.get('result')

        if result is True:
            self.render(f"Contact with name '{name}' has been deleted")
        else:
            self.render(f"Contact not found")

    @observer(Observers.AddNotes)
    def add_notes_result(self, **kwargs):
        # Відображає результат додавання нотаток
        name = kwargs.get('result')

        self.render(f"Notes for {name} added.")

    @observer(Observers.ShowNotes)
    def show_notes_result(self, **kwargs):
        # Відображає нотатки для вказаного контакту
        name, notes = kwargs.get('result')

        self.render(f"{name}'s notes:\n{notes}" if notes else f"{name} has no notes recorded.")

    def add_tag(self):
        # Запитує ім'я контакту, індекс нотатки та тег для додавання
        while True:
            name = input_string("Enter contact name: ")
            if not self.__model__.find(name):
                print(f"Contact with name '{name}' does not exist. Please enter a valid contact name.")
            else:
                break
        note_index = input_number("Enter note index to add tag: ")
        tag = input_string("Enter tag to add: ")
        return name, note_index, tag