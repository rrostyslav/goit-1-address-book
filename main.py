from src.decorators.handle_error import handle_error  # Імпортує декоратор для обробки помилок
from src.utils.valid_input import input_string, input_number  # Імпортує функції для введення та валідації даних
from src.view import View  # Імпортує клас View для роботи з інтерфейсом користувача
from src.models.address_book import load_data  # Імпортує функцію для завантаження даних адресної книги
from src.controller import Controller  # Імпортує клас Controller для управління даними

def main():
    # Завантажує дані адресної книги з файлу
    address_book = load_data()
    # Створює об'єкт View для відображення інформації, використовуючи завантажені дані
    view = View(address_book)
    # Створює об'єкт Controller для управління адресною книгою, використовуючи дані та об'єкт View
    controller = Controller(address_book, view)

    # Виводить меню з основними опціями
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
    print("13. Edit note")
    print("14. Delete note")
    print("15. Add tag to notes")
    print("16. Search notes by tag")

    while True:
        try:
            # Запитує у користувача вибір номера опції з діапазону від 0 до 12
            option = input_number(
                prompt="Select option number: ",
                min_value=0,
                max_value=16,
            )

            # Виконує відповідну дію, залежно від вибраної опції
            match option:
                case 1:
                    controller.add_contact()  # Додає новий контакт
                case 2:
                    controller.show_phone()  # Показує телефон контакту
                case 3:
                    controller.show_all_contacts()  # Показує всі контакти
                case 4:
                    controller.change_contact_phone()  # Змінює телефон контакту
                case 5:
                    controller.add_birthday()  # Додає день народження до контакту
                case 6:
                    controller.show_birthday()  # Показує дату народження контакту
                case 7:
                    controller.add_email()  # Додає електронну адресу до контакту
                case 8:
                    controller.add_address()  # Додає адресу до контакту
                case 9:
                    controller.show_birthdays_in_days()  # Показує дні народжень у зазначений період
                case 10:
                    controller.change_contact_name()  # Змінює ім'я контакту
                case 11:
                    controller.add_notes()  # Додає нотатки до контакту
                case 12:
                    controller.show_notes()  # Показує нотатки
                case 13:
                    controller.edit_note()
                case 14:
                    controller.delete_note()    
                case 15:
                    controller.add_tag()  # Додає тег до існуючої нотатки
                case 16:
                    controller.search_notes_by_tag()  # Пошук нотаток за тегами
                case 0:
                    # Завершує роботу програми, зберігаючи дані адресної книги
                    print("Good bye")
                    address_book.save_data()
                    break
        except KeyboardInterrupt:
            # Обробляє завершення програми при натисканні Ctrl+C, зберігаючи дані адресної книги
            print("\nGood bye") 
            address_book.save_data()
            break

# Основна точка входу в програму
if __name__ == "__main__":
    main()
