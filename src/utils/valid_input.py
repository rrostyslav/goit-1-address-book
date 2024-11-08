from src.utils.validations import validate_email, validate_phone


def input_number(
        prompt: str,
        min_value: int = None,
        max_value: int = None,
        error_message: str = "Invalid number"
) -> int:
    while True:
        user_input = input(prompt)

        if user_input.isdigit():
            number = int(user_input)
            if (min_value is not None and number < min_value) or (max_value is not None and number > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return number
        else:
            print(error_message)


def input_string(prompt: str, allow_empty: bool = False, error_message: str = "Invalid text") -> str:
    while True:
        user_input = input(prompt)

        if user_input and (allow_empty or user_input.strip()):
            return user_input
        else:
            print("Text input cannot be empty." if not allow_empty else error_message)


def input_email(prompt: str, error_message: str = "Invalid email") -> str:
    while True:
        user_input = input(prompt)

        if validate_email(user_input):
            return user_input
        else:
            print(error_message)

def input_phone(prompt: str, error_message: str = "Invalid phone number format. Use +380XXXXXXXXX") -> str:
    while True:
        user_input = input(prompt)

        if validate_phone(user_input):
            return user_input
        else:
            print(error_message)
