from src.models.record import Record  # Імпортує клас Record, що представляє запис контакту
from src.models.address_book import AddressBook  # Імпортує клас AddressBook, що представляє книгу контактів
from src.view import View  # Імпортує клас View для взаємодії з користувачем


class Controller:
    # Ініціалізує контролер з моделлю AddressBook та представленням View
    def __init__(self, model: AddressBook, view: View):
        self.model = model
        self.view = view

    # Додає контакт до адресної книги
    def add_contact(self):
        # Отримує ім'я та телефон від користувача через View
        name, phone = self.view.add_contact()

        # Шукає контакт у моделі за ім'ям
        contact: Record = self.model.find(name)

        # Якщо контакт не знайдений, створює новий запис
        if not contact:
            contact = Record(name)
        # Додає телефон до запису
        contact.add_phone(phone)

        # Додає або оновлює запис у моделі
        self.model.add_record(contact)

    # Показує телефон контакту
    def show_phone(self):
        # Отримує ім'я контакту від користувача
        name = self.view.show_phone()
        # Викликає метод моделі для відображення телефону
        self.model.show_phone(name)

    # Показує всі контакти
    def show_all_contacts(self):
        self.model.show_all_contacts()

    # Змінює ім'я контакту
    def change_contact_name(self):
        # Отримує старе та нове ім'я від користувача
        old_name, new_name = self.view.change_contact_name()
        try:
            # Викликає метод моделі для зміни імені контакту
            self.model.change_contact_name(old_name, new_name)
        except ValueError as e:
            # Відображає повідомлення про помилку, якщо зміна не вдалася
            self.view.render(e)

    # Змінює номер телефону контакту
    def change_contact_phone(self):
        # Отримує ім'я контакту, старий та новий номер телефону
        name, old_phone, new_phone = self.view.change_contact_phone()
        # Викликає метод моделі для зміни телефону
        self.model.change_contact_phone(name, old_phone, new_phone)

    # Додає дату народження до контакту
    def add_birthday(self):
        # Отримує ім'я та дату народження від користувача
        name, birthday = self.view.add_birthday()
        # Викликає метод моделі для додавання дня народження
        self.model.add_birthday(name, birthday)

    # Показує дату народження контакту
    def show_birthday(self):
        # Отримує ім'я контакту від користувача
        name = self.view.show_birthday()
        # Викликає метод моделі для показу дня народження
        self.model.show_birthday(name)

    # Додає електронну адресу до контакту
    def add_email(self):
        # Отримує ім'я та електронну адресу від користувача
        name, email = self.view.add_email()
        # Викликає метод моделі для додавання електронної адреси
        self.model.add_email(name, email)

    # Додає адресу до контакту
    def add_address(self):
        # Отримує ім'я та адресу від користувача
        name, address = self.view.add_address()
        # Викликає метод моделі для додавання адреси
        self.model.add_address(name, address)

    # Показує контакти, які мають дні народжень у зазначений період
    def show_birthdays_in_days(self):
        # Отримує кількість днів від користувача
        days = self.view.show_birthdays_in_days()
        # Викликає метод моделі для показу днів народжень у межах цього періоду
        self.model.show_birthdays_in_days(days)

    # Видаляє контакт з адресної книги
    def delete_contact(self):
        # Отримує ім'я контакту, який треба видалити
        name = self.view.delete_contact()
        # Викликає метод моделі для видалення контакту
        self.model.delete_contact(name)

    # Додає нотатки до контакту
    def add_notes(self):
        # Отримує ім'я контакту та нотатки від користувача
        name, notes = self.view.add_notes()
        # Викликає метод моделі для додавання нотаток
        self.model.add_notes(name, notes)

    # Показує нотатки для контакту
    def show_notes(self):
        # Отримує ім'я контакту від користувача
        name = self.view.show_notes()
        # Викликає метод моделі для показу нотаток
        self.model.show_notes(name)
