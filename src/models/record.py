from src.models.birthday import Birthday
from src.models.name import Name
from src.models.phone import Phone
from src.models.address import Address
from src.models.notes import Notes
from src.models.email import Email

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None
        self.notes = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def add_notes(self, note):
        self.notes.append(Notes(note))

    def get_notes(self):
        return "\n".join(str(note) for note in self.notes) if self.notes else None

    def get_birthday(self):
        return self.birthday.value if self.birthday else None

    def delete_note(self, note_id):
        del self.notes[note_id]