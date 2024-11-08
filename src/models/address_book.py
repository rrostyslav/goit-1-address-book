from datetime import datetime, timedelta
from src.models.name import Name
from src.decorators.observable import observable, notify_observers
from src.constants.observers import Observers
from src.models.record import Record
import pickle


@observable
class AddressBook:
    def __init__(self):
        self.contacts = {}

    @notify_observers(Observers.AddContact)
    def add_record(self, record):
        self.contacts[record.name.value] = record
        return True

    def find(self, name):
        return self.contacts.get(name)

    @notify_observers(Observers.ShowPhone)
    def show_phone(self, name):
        record: Record = self.find(name)

        if record is not None:
            return record.phones
        return None

    @notify_observers(Observers.ShowAllContacts)
    def show_all_contacts(self):
        if not self.contacts:
            return None
        return {name: [phone.value for phone in record.phones] for name, record in self.contacts.items()}
    
    @notify_observers(Observers.ChangeContactName)
    def change_contact_name(self, old_name, new_name):
        record = self.contacts.pop(old_name, None)

        if record is None:
            return print("Contact not found.")
        if new_name in self.contacts:
            return print("A contact with the new name already exists.")

        record.name = Name(new_name)
        self.contacts[new_name] = record
        return new_name

    @notify_observers(Observers.ChangeContactPhone)
    def change_contact_phone(self, name, old_phone, new_phone):

        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        for phone_record in record.phones:
            if phone_record.value == old_phone:
                phone_record.value = new_phone
                return name, old_phone, new_phone
        raise ValueError(f"Phone {old_phone} not found for {name}.")

    @notify_observers(Observers.AddBirthday)
    def add_birthday(self, name, birthday):
        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        record.add_birthday(birthday)
        return name, birthday

    @notify_observers(Observers.ShowBirthday)
    def show_birthday(self, name):
        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        birthday = record.get_birthday()
        return name, birthday

    @notify_observers(Observers.AddEmail)
    def add_email(self, name, email):
        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        record.add_email(email)

        return name, email

    @notify_observers(Observers.AddAddress)
    def add_address(self, name, address):
        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        record.add_address(address)

        return name, address

    @notify_observers(Observers.ShowBirthdaysInDays)
    def show_birthdays_in_days(self, days):
        contacts_with_upcoming_birthdays = []
        target_date = datetime.now() + timedelta(days=days)
        current_year = datetime.now().year

        for record in self.contacts.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=current_year)

                if birthday_this_year.date() <= target_date.date():
                    contacts_with_upcoming_birthdays.append(record.name.value)

        return contacts_with_upcoming_birthdays

    @notify_observers(Observers.DeleteContact)
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        else:
            raise ValueError("Contact not found.")

    @notify_observers(Observers.AddNotes)
    def add_notes(self, name, notes):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        record.add_notes(notes)

        return name

    @notify_observers(Observers.ShowNotes)
    def show_notes(self, name):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        notes = record.get_notes()

        return name, notes
    
    @notify_observers(Observers.SaveData)
    def save_data(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
           pickle.dump(self, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()       
