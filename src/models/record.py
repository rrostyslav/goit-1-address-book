from src.models.birthday import Birthday
from src.models.name import Name
from src.models.phone import Phone
from src.models.address import Address
from src.models.notes import Notes
from src.models.email import Email

class Record:
    def __init__(self, name):
        self.name = Name(name)  # Ім'я контакту, створюється об'єкт Name
        self.phones = []  # Список телефонів контакту
        self.birthday = None  # День народження контакту
        self.email = None  # Електронна адреса контакту
        self.address = None  # Адреса контакту
        self.notes = []  # Список нотаток

    # Метод для додавання телефону
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Метод для додавання дня народження
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    # Метод для додавання електронної адреси
    def add_email(self, email):
        self.email = Email(email)

    # Метод для додавання адреси
    def add_address(self, address):
        self.address = Address(address)

    # Метод для додавання нотаток
    def add_notes(self, notes):
        note = Notes(notes)
        self.notes.append(note)

    # Метод для отримання нотаток
    def get_notes(self):
        return "\n".join(str(note) for note in self.notes) if self.notes else None

    # Метод для отримання дня народження
    def get_birthday(self):
        return self.birthday.value if self.birthday else None