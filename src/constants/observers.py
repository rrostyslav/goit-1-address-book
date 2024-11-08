from enum import Enum

class Observers(Enum):
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