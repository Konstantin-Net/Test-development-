documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': ["34"]
}


def people(num):   # Функция выдачи имени по номеру документа
    for dic in documents:
        if num in dic.values():
            return dic.get("name")
    else:
        print("В базе нет такого документа")


def shelf(num):   # Функция выдачи номера полками по номеру документа
    for k, v in directories.items():
        if num in v:
            return k
    else:
        print("В базе нет такого документа")


def lst():  # Функция выдачи свписка всех документов
    for dic in documents:
        print(*list(dic.values()))


def add(typ, num, nam, she):   # Функция редактирования словаря и списка
    documents.append({"type": typ, "number": num, "name": nam})
    while int(she) > len(directories.keys()):
        she = input(f"Для хранения доступно полки {', '.join(list(directories.keys()))}. Введите номер одной из них:")
    directories[she].append(num)
    print("Новый документ добавлен в базу")


def delete(num):    # Функция удаления документа по номеру
    for dic in documents:
        if num in dic.values():
            documents.remove(dic)
    for k, v in directories.items():
        if num in v:
            v.remove(num)
            print("Документ удалён из базы")
            break
    else:
        print("В базе нет такого документа")


def move(num, she):   # Функция перемещает документ на другую полку
    x = 0
    if she not in directories.keys():
        print("Такой полки не существует")
        return
    for v in directories.values():
        if num in v:
            v.remove(num)
            directories[she].append(num)
            print(f"Документ перемещён на {she} полку")
            x = 1
            break
    if x == 0:
        print("В базе нет такого документа")


def add_shelf(she):     # Функция добавления новой полки в перечень
    if she in directories.keys():
        print("Полка под таким номером уже существует")
    else:
        directories[she] = []
        print(f"Полка номер {she} создана")


def main():     # Функция диспетчеризации пользовательского ввода
    while True:
        user_input = input("Введите команду: ")
        if user_input == "p":
            num = input("Введите номер документа:  ")
            return people(num)
        elif user_input == "s":
            num = input("Введите номер документа:  ")
            return shelf(num)
        elif user_input == "l":
            return lst()
        elif user_input == "a":
            typ = input("Введите тип документа: ")
            num = input("Введите номер документа: ")
            nam = input("Введите имя владельца: ")
            she = input("Введите номер полки для хранения документа: ")
            return add(typ, num, nam, she)
        elif user_input == "d":
            num = input("Введите номер документа: ")
            return delete(num)
        elif user_input == "m":
            num = input("Введите номер документа: ")
            she = input("Введите номер полки на которую требуется переместить документ:  ")
            return move(num, she)
        elif user_input == "as":
            she = input("Введите номер полки которую требуется создать:  ")
            return add_shelf(she)
        else:
            print("Такой команды нет. Список доступных команд 'p', 's', 'l', 'a', 'd', 'm', 'as'")


# d = {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
# print(d in documents and "34" in directories.get("3"))

# while True:
#     main()
#     print()

