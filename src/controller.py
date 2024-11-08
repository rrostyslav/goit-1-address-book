from src.models.record import Record
from src.models.address_book import AddressBook
from src.view import View


class Controller:
    def __init__(self, model: AddressBook, view: View):
        self.model = model
        self.view = view

    def add_contact(self):
        name, phone = self.view.add_contact()

        contact: Record = self.model.find(name)

        if not contact:
            contact = Record(name)
        contact.add_phone(phone)

        self.model.add_record(contact)

    def show_phone(self):
        name = self.view.show_phone()
        self.model.show_phone(name)

    def show_all_contacts(self):
        self.model.show_all_contacts()

    def change_contact_name(self):
        old_name, new_name = self.view.change_contact_name()
        try:
            self.model.change_contact_name(old_name, new_name)
        except ValueError as e:
            self.view.render(e)

    def change_contact_phone(self):
        name, old_phone, new_phone = self.view.change_contact_phone()
        self.model.change_contact_phone(name, old_phone, new_phone)

    def add_birthday(self):
        name, birthday = self.view.add_birthday()
        self.model.add_birthday(name, birthday)

    def show_birthday(self):
        name = self.view.show_birthday()
        self.model.show_birthday(name)

    def add_email(self):
        name, email = self.view.add_email()
        self.model.add_email(name, email)

    def add_address(self):
        name, address = self.view.add_address()
        self.model.add_address(name, address)

    def show_birthdays_in_days(self):
        days = self.view.show_birthdays_in_days()
        self.model.show_birthdays_in_days(days)

    def delete_contact(self):
        name = self.view.delete_contact()
        self.model.delete_contact(name)

    def add_notes(self):
        name, notes = self.view.add_notes()
        self.model.add_notes(name, notes)

    def show_notes(self):
        name = self.view.show_notes()
        self.model.show_notes(name)

    def delete_note(self):
        name, index = self.view.delete_note()
        try:
            self.model.delete_note(name, index)
        except Exception as e:
            print(e)


    def edit_note(self):
        name, index, new_note = self.view.edit_note()
        try:
            self.model.edit_note(name, index, new_note)
        except Exception as e:
            print(e)
