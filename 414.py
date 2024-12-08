import random
import string

def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation #буквы + цифры + пунктуация

    length = int(input("Введите длину пароля"))
    password = ''

    for i in range(length):
        password += random.choice(alphabet)

    return password

def read(storage):
    for i in range(len(storage[0])):
        print(storage[0][i])
    for i in range(len(storage[1])):
        print(storage[1][i])
    for i in range(len(storage[2])):
        print(storage[2][i])
    for i in range(len(storage[3])):
        print(storage[3][i])
    return 0

storage = [["id"], ["login"], ["password"], ["about"]]

while True:
    answer = input("Что вы хотите сделать? 0 - выйти, 1 - создать нового пользователя, "
          "2 - удалить пользователя, 3 - изменить пользователя, 4 - вывести все логины пароли")

    if answer == "0":
        break
    elif answer == "1":
       storage[0].append(str(random.randint(0, 10000))) #Добавляем id
       storage[1].append(input("Введите ваш логин"))
       storage[2].append(generate_password())
       storage[3].append(input("Расскажите о себе"))
    elif answer == "2":
        id = input("Введите id для удаления")
        ind = storage[0].index(id)
        storage[0].pop(ind)
        storage[1].pop(ind)
        storage[2].pop(ind)
        storage[3].pop(ind)
    elif answer == "3":
        pass
    elif answer == "4":
        print(read(storage))


