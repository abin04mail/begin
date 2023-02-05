import argparse
import json

book = json.load( open( '/home/serg/phone_book' ))

parser = argparse.ArgumentParser(description='Telephon book')
parser.add_argument('-a', '--add', dest="param1")
parser.add_argument('-d', '--delete', dest="param2")
parser.add_argument('-s', '--show', dest="param3", default="all")

args = parser.parse_args()
# print(args)

# Формат запуска python3.11 /home/serg/'Рабочий стол'/Python71-1/begin/phone_book.py --add "Katya:89123456713"
if args.param1:
    name, tele = args.param1.split(":")
    print(name, tele)
    if name in book:
        book[name] = [int(tele)]
        print("Контакт с именем ", name, " обновлен")
        print(name, ":", book[name])
    else:
        book[name] = int(tele)
        print("Контакт с именем ", name, "добавлен")
        print(name, ":", book[name])
        print(book)

    # Формат запуска python3.11 /home/serg/'Рабочий стол'/Python71-1/begin/phone_book.py --delete "Katya"
elif args.param2:
        name = args.param2
        if name in book:
            del book[name]
            print("Контакт с именем ", name, " удален")
        else:
            print("Контакта с именем ", name, " в книге нет")

    # Формат запуска python3.11 /home/serg/'Рабочий стол'/Python71-1/begin/phone_book.py --show "Katya" или --show "all"
elif args.param3:
        name = args.param3
        if name == 'all':
            print(book)
        elif name in book:
            print(name, ":", book[name])
        else:
            print("Контакта с именем ", name, " в книге нет")
else:
     print("Введен неверный аргумент")
json.dump( book, open( '/home/serg/phone_book', "w"))