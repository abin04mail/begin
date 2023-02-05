import argparse
book = {"Masha": 89778881539, "Pasha": 89778081476, "Natasha": 89771231536}

parser = argparse.ArgumentParser(description='Telephon book')
parser.add_argument('-a', '--add', dest="param1")
parser.add_argument('-d', '--delete', dest="param2")
parser.add_argument('-s', '--show', dest="param3", default="all")

args = parser.parse_args()
print(args)

# Формат запуска python3.11 /home/serg/'Рабочий стол'/Python71-1/begin/phone_book.py --add "Katya:89123456713"
if args.param1:
    name, tele = args.param1.split(":")
    if name in book:
        book[name] = [book.get(name), int(tele)]
        print("Контакт с именем ", name, " обновлен")
        print(name, ":", book[name])
    else:
        book[name] = int(tele)
        print("Контакт с именем ", name, "добавлен")
        print(name, ":", book[name])

# Формат запуска python3.11 /home/serg/'Рабочий стол'/Python71-1/begin/phone_book.py --delete "Katya"
if args.param2:
    name = args.param2
    if name in book:
        del[book][name]
        print("Контакт с именем ", name, " удален")
    else:
        print("Контакта с именем ", name, " в книге нет")

# Формат запуска python3.11 /home/serg/'Рабочий стол'/Python71-1/begin/phone_book.py --show "Katya" или --show "all"
if args.param3:
    name = args.param3
    #if name == all:
    #    print(name, ":", book[name])
    if name in book:
        print(book[name])
    else:
        print("Контакта с именем ", name, " в книге нет")
