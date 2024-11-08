from enum import Enum

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