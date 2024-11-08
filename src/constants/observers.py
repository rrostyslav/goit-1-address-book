from enum import Enum  # Імпортує клас Enum для створення перерахування

# Клас Observers, що представляє типи сповіщень для спостерігачів
class Observers(Enum):
    LoadData = 'LoadData'
    SaveData = 'SaveData'
    AddContact = 'AddContact'
    ShowPhone = 'ShowPhone'
    ShowBirthdaysInDays = 'BirthdaysInDays'
    ChangeContactName = 'ChangeContactName'
    DeleteContact = 'DeleteContact'
    AddBirthday = 'AddBirthday'
    AddEmail = 'AddEmail'
    AddAddress = 'AddAddress'
    ShowBirthday = 'ShowBirthday'
    AddNotes = 'AddNotes'
    ShowNotes = 'ShowNotes'
    ChangeContactPhone = 'ChangeContactPhone'
    ShowAllContacts = 'ShowAllContacts'
    DeleteNote = 'DeleteNote'
    EditNote = 'EditNote'