phones = {} #Словарь, в нём хранится информация о контактах

def add_contact(phone_number, name): #добавление нового контакта
    phone_number = str(phone_number)
    if (len(phone_number) == 11 or len(phone_number) == 12) and len(name) > 0:
        print("Контакт добавлен")
        return phones.update({phone_number: name})
    else:
        return "Ошибка при добавлении контакта"

def del_contact(phone_number):
    phone_number = str(phone_number)
    if len(phone_number) == 11 or len(phone_number) == 12:
        print("Контакт удалён")
        return phones.pop(phone_number)
    else:
        return "Ошибка при удалении контакта"

def edit_contact(contact):
    answer = input("Что вы хотите отредактировать? 1 - номер, 2 - имя")
    if answer == "1":
        name = phones[contact]
        del_contact(contact)
        add_contact(input("Введите новый номер"), name)
        return "Номер отредактирован"
    elif answer == "2":
        phones[contact] = input("Введите новое имя")
        return "Имя изменено"

def get_contact(phone_number):
    return phones.get(phone_number)

def get_all():
    return phones

add_contact(89056319203, "Егор")
print(phones)
