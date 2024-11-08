from src.utils.validations import validate_email, validate_phone  # Імпортує функції валідації для електронної пошти та телефону

# Функція для введення та перевірки числового значення
def input_number(
        prompt: str,
        min_value: int = None,
        max_value: int = None,
        error_message: str = "Invalid number"
) -> int:
    while True:
        user_input = input(prompt)  # Запитує користувача на введення

        if user_input.isdigit():
            number = int(user_input)
            # Перевіряє, чи число відповідає вказаним межам, якщо такі задані
            if (min_value is not None and number < min_value) or (max_value is not None and number > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return number  # Повертає введене число, якщо воно є валідним
        else:
            print(error_message)  # Виводить повідомлення про помилку, якщо введено не число

# Функція для введення та перевірки текстового значення
def input_string(prompt: str, allow_empty: bool = False, error_message: str = "Invalid text") -> str:
    while True:
        user_input = input(prompt)  # Запитує користувача на введення

        # Перевіряє, чи введено значення і чи дозволені пусті рядки
        if user_input and (allow_empty or user_input.strip()):
            return user_input  # Повертає введений текст
        else:
            # Виводить відповідне повідомлення про помилку, залежно від налаштувань
            print("Text input cannot be empty." if not allow_empty else error_message)

# Функція для введення та перевірки електронної адреси
def input_email(prompt: str, error_message: str = "Invalid email") -> str:
    while True:
        user_input = input(prompt)  # Запитує користувача на введення електронної адреси

        if validate_email(user_input):
            return user_input  # Повертає введену електронну адресу, якщо вона є валідною
        else:
            print(error_message)  # Виводить повідомлення про помилку, якщо валідація не пройшла

# Функція для введення та перевірки номера телефону
def input_phone(prompt: str, error_message: str = "Invalid phone number format. Use +380XXXXXXXXX") -> str:
    while True:
        user_input = input(prompt)  # Запитує користувача на введення номера телефону

        if validate_phone(user_input):
            return user_input  # Повертає введений номер телефону, якщо він є валідним
        else:
            print(error_message)  # Виводить повідомлення про помилку, якщо валідація не пройшла
