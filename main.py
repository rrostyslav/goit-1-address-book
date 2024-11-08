from src.decorators.handle_error import handle_error
from src.utils.valid_input import input_string, input_number
from src.view import View
from src.models.address_book import load_data
from src.controller import Controller



def main():
    address_book = load_data()
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
    print("13. Edit notes")  # Новий пункт для редагування нотаток
    print("14. Delete note")  # Новий пункт для видалення нотаток

    while True:
        try:
            option = input_number(
                prompt="Select option number: ",
                min_value=0,
                max_value=14,  # Оновлено максимальне значення
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
                case 13:
                    controller.edit_notes()  # Виклик нового методу редагування нотаток
                case 14:
                    controller.delete_note()  # Виклик нового методу видалення нотаток
                case 0:
                    print("Good bye")
                    address_book.save_data()
                    break
        except KeyboardInterrupt:
            print("\nGood bye")
            address_book.save_data()
            break

if __name__ == "__main__":
    main()