from enum import Enum  # Імпортує клас Enum для створення перерахування

# Клас Observers, що представляє типи сповіщень для спостерігачів
class Observers(Enum):
    LoadData = 'LoadData'  # Сповіщення для завантаження даних
    SaveData = 'SaveData'  # Сповіщення для збереження даних
    AddContact = 'AddContact'  # Сповіщення для додавання нового контакту
    ShowPhone = 'ShowPhone'  # Сповіщення для показу номера телефону
    ShowBirthdaysInDays = 'BirthdaysInDays'  # Сповіщення для показу днів народжень у певний період
    ChangeContactName = 'ChangeContactName'  # Сповіщення для зміни імені контакту
    DeleteContact = 'DeleteContact'  # Сповіщення для видалення контакту
    AddBirthday = 'AddBirthday'  # Сповіщення для додавання дня народження
    AddEmail = 'AddEmail'  # Сповіщення для додавання електронної адреси
    AddAddress = 'AddAddress'  # Сповіщення для додавання адреси
    ShowBirthday = 'ShowBirthday'  # Сповіщення для показу дня народження контакту
    AddNotes = 'AddNotes'  # Сповіщення для додавання нотаток
    ShowNotes = 'ShowNotes'  # Сповіщення для показу нотаток контакту
    ChangeContactPhone = 'ChangeContactPhone'  # Сповіщення для зміни номера телефону контакту
    ShowAllContacts = 'ShowAllContacts'  # Сповіщення для показу всіх контактів
    AddNoteTags = "AddNoteTags"
    ShowTags = "ShowTags"