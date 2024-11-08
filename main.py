from src.decorators.handle_error import handle_error
from src.utils.valid_input import input_string, input_number
from src.view import View
from src.models.address_book import AddressBook
from src.models.record import Record

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


def main():
    address_book = AddressBook()
    view = View(address_book)
    controller = Controller(address_book, view)

    print("Main menu:")
    print("1. Add contact")
    print("2. Show phone")
    print('3. Show all contacts')
    print("4. Change contact")
    print("5. Add birthday")
    print("6. Show birthday")
    print("7. Add email")
    print("8. Add address")
    print("9. Show birthdays in days")
    print("10. Change name of contact")
    print("11. Add notes")
    print("12. Show notes")

    while True:
        try:
            option = input_number(
                prompt="Select option number: ",
                min_value=0,
                max_value=12,
            )

            match option:
                case 1:
                    controller.add_contact()
                case 2:
                    controller.show_phone()
                case 3:
                    controller.show_all_contacts()
                case 4:
                    controller.change_contact_phone()
                case 5:
                    controller.add_birthday()
                case 6:
                    controller.show_birthday()
                case 7:
                    controller.add_email()
                case 8:
                    controller.add_address()
                case 9:
                    controller.show_birthdays_in_days()
                case 10:
                    controller.change_contact_name()
                case 11:
                    controller.add_notes()
                case 12:
                    controller.show_notes()
                case 0:
                    break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()