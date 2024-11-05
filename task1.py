from datetime import datetime, timedelta
import re
import pickle

class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number format. Use +380XXXXXXXXX")
        super().__init__(phone)

    @staticmethod
    def validate_phone(phone):
        return bool(re.match(r'^\+380\d{9}$', phone))


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Email(Field):
    def __init__(self, email):
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        super().__init__(email)

    @staticmethod
    def validate_email(email):
        return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))


class Address(Field):
    def __init__(self, address):
        if not isinstance(address, str) or not address:
            raise ValueError("Address must be a non-empty string")
        super().__init__(address)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None


    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        
    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def get_birthday(self):
        return self.birthday.value if self.birthday else None


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_record(self, record):
        self.contacts[record.name.value] = record

    def find(self, name):
        return self.contacts.get(name)

    def get_birthdays_in_days(self, days):
        contacts_with_upcoming_birthdays = []
        target_date = datetime.now() + timedelta(days=days)
        current_year = datetime.now().year

        for record in self.contacts.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=current_year)
                
                if birthday_this_year.date() == target_date.date():
                    contacts_with_upcoming_birthdays.append(record.name.value)

        return contacts_with_upcoming_birthdays
    
    def change_name(self, old_name, new_name):
        record = self.contacts.pop(old_name, None)
        if record is None:
            raise ValueError("Contact not found.")
        if new_name in self.contacts:
            raise ValueError("A contact with the new name already exists.")
        
        record.name = Name(new_name)
        self.contacts[new_name] = record
        return f"Contact name changed from {old_name} to {new_name}."

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact {name} deleted."
        else:
            raise ValueError("Contact not found.")

def birthdays_in_days(args, book: AddressBook):
    if len(args) < 1:
        return "Please provide the number of days."
    try:
        days = int(args[0])
    except ValueError:
        return "Please provide a valid number of days."

    contacts = book.get_birthdays_in_days(days)
    if not contacts:
        return f"No contacts with birthdays in {days} days."
    return f"Contacts with birthdays in {days} days: " + ", ".join(contacts)


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return wrapper

@input_error
def change_contact_name(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Please provide both the current name and the new name.")
    old_name, new_name = args
    return book.change_name(old_name, new_name)


@input_error
def delete_contact(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("Please provide the name of the contact to delete.")
    name = args[0]
    return book.delete_contact(name)


@input_error
def add_birthday(args, book):
    if len(args) < 2:
        raise ValueError("Please provide both name and birthday.")
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found.")
    record.add_birthday(birthday)
    return f"Birthday for {name} added."

@input_error
def add_email(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Please provide both name and email.")
    name, email = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found.")
    record.add_email(email)
    return f"Email for {name} added."

@input_error
def add_address(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Please provide both name and address.")
    name, address = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found.")
    record.add_address(address)
    return f"Address for {name} added."

@input_error
def show_birthday(args, book):
    if len(args) < 1:
        raise ValueError("Please provide a name.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found.")
    birthday = record.get_birthday()
    return f"{name}'s birthday is on {birthday.strftime('%d.%m.%Y')}" if birthday else f"{name} has no birthday recorded."


@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays."
    return "Upcoming birthdays: " + ", ".join(upcoming_birthdays)


def parse_input(user_input):
    return user_input.split()


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() 


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))
        
        elif command == "add-email":
            print(add_email(args, book))

        elif command == "add-address":
            print(add_address(args, book))
            
        elif command == "birthdays-in-days":
            print(birthdays_in_days(args, book))

        elif command == "change-name":
            print(change_contact_name(args, book))

        elif command == "delete":
            print(delete_contact(args, book))
            
        else:
            print("Invalid command.")


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Please provide both name and phone number.")
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 3:
        raise ValueError("Please provide name, old phone number, and new phone number.")
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found.")
    for phone_record in record.phones:
        if phone_record.value == old_phone:
            phone_record.value = new_phone
            return f"Updated {name}'s phone from {old_phone} to {new_phone}."
    raise ValueError(f"Phone {old_phone} not found for {name}.")


@input_error
def show_phone(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("Please provide a name.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError("Contact not found.")
    phones = ", ".join(phone.value for phone in record.phones)
    return f"{name}'s phone numbers: {phones}"


@input_error
def show_all_contacts(book: AddressBook):
    if not book.contacts:
        return "No contacts in the address book."
    return "\n".join([f"{name}: {', '.join(phone.value for phone in record.phones)}" for name, record in book.contacts.items()])


if __name__ == "__main__":
    main()
