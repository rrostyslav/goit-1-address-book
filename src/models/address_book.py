from datetime import datetime, timedelta  # Імпортує datetime для роботи з датами та timedelta для роботи з періодами часу
from src.models.name import Name  # Імпортує клас Name для роботи з іменами контактів
from src.decorators.observable import observable, notify_observers  # Імпортує декоратори для патерну "спостерігач"
from src.constants.observers import Observers  # Імпортує константи для сповіщень спостерігачів
from src.models.record import Record  # Імпортує клас Record для роботи з контактами
import pickle  # Імпортує модуль для серіалізації та десеріалізації даних

# Клас AddressBook, що представляє адресну книгу контактів
@observable
class AddressBook:
    def __init__(self):
        self.contacts = {}  # Словник для зберігання контактів

    # Метод для додавання нового запису до адресної книги
    @notify_observers(Observers.AddContact)
    def add_record(self, record):
        self.contacts[record.name.value] = record
        return True

    # Метод для пошуку контакту за ім'ям
    def find(self, name):
        return self.contacts.get(name)

    # Метод для показу телефону контакту
    @notify_observers(Observers.ShowPhone)
    def show_phone(self, name):
        record: Record = self.find(name)

        if record is not None:
            return record.phones
        return None

    # Метод для показу всіх контактів
    @notify_observers(Observers.ShowAllContacts)
    def show_all_contacts(self):
        if not self.contacts:
            return None
        return {name: [phone.value for phone in record.phones] for name, record in self.contacts.items()}

    # Метод для зміни імені контакту
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

    # Метод для зміни номера телефону контакту
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

    # Метод для додавання дня народження до контакту
    @notify_observers(Observers.AddBirthday)
    def add_birthday(self, name, birthday):
        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        record.add_birthday(birthday)
        return name, birthday

    # Метод для показу дня народження контакту
    @notify_observers(Observers.ShowBirthday)
    def show_birthday(self, name):
        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        birthday = record.get_birthday()
        return name, birthday

    # Метод для додавання електронної адреси до контакту
    @notify_observers(Observers.AddEmail)
    def add_email(self, name, email):
        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        record.add_email(email)
        return name, email

    # Метод для додавання адреси до контакту
    @notify_observers(Observers.AddAddress)
    def add_address(self, name, address):
        record = self.find(name)
        if record is None:
            print("Contact not found.")
            return
        record.add_address(address)
        return name, address

    # Метод для показу контактів, які мають дні народжень у зазначений період
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

    # Метод для видалення контакту з адресної книги
    @notify_observers(Observers.DeleteContact)
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        else:
            raise ValueError("Contact not found.")

    # Метод для додавання нотаток до контакту
    @notify_observers(Observers.AddNotes)
    def add_notes(self, name, notes):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        record.add_notes(notes)
        return name

    # Метод для додавання тегу до нотаток контакту
    @notify_observers(Observers.AddNoteTags)
    def add_tag(self, name, note_index, tag):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        if hasattr(record, 'notes') and record.notes is not None:
            if note_index < 0 or note_index >= len(record.notes):
                raise ValueError("Invalid note index.")
            record.notes[note_index].add_tag(tag)
            return name, note_index, tag
        else:
            raise ValueError("No notes found for this contact.")

    # Метод для пошуку нотаток за тегом
    @notify_observers(Observers.ShowTags)
    def search_notes_by_tag(self, tag):
        notes_with_tag = []
        for record in self.contacts.values():
            if hasattr(record, 'notes') and record.notes is not None:
                for note in record.notes:
                    if note.has_tag(tag):
                        notes_with_tag.append(record.name.value)
                        break
        return notes_with_tag
    
    # Метод для показу нотаток контакту
    @notify_observers(Observers.ShowNotes)
    def show_notes(self, name):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        notes = record.get_notes()
        return name, notes

    # Метод для збереження даних адресної книги у файл
    @notify_observers(Observers.SaveData)
    def save_data(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)


    @notify_observers(Observers.DeleteNote)
    def delete_note(self, name, index):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        record.delete_note_by_index(index - 1)
        return index, name

    @notify_observers(Observers.EditNote)
    def edit_note(self, name, index, new_note):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        record.edit_note_by_index(index - 1, new_note)  # Adjusting for 1-based index
        return index, name

    # Функція для завантаження даних адресної книги з файлу
    
        
    @notify_observers(Observers.DeleteNote)
    def delete_note(self, name, index):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        record.delete_note_by_index(index - 1)
        return index, name
    
    @notify_observers(Observers.EditNote)
    def edit_note(self, name, index, new_note):
        record = self.find(name)
        if record is None:
            raise ValueError("Contact not found.")
        record.edit_note_by_index(index - 1, new_note)  # Adjusting for 1-based index
        return index, name   

    
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()      