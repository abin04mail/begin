# class Student:
#     def __init__(self, name='Ivanov', group_number=2203, age=21):
#         self.name=name
#         self.group_number=group_number
#         self.age=age
#     def getName(self):
#         return self.name
#     def getAge(self):
#         return self.age
#     def getGroupNumber(self):
#         return self.group_number
#     def setNameAge(self,name,age):
#         self.name=name
#         self.age=age
#     def setGroupNumber(self,groupNumber):
#         self.group_number=groupNumber
# stud1=Student('Ivanov',2203,20)
# stud2=Student('Petrov',2203,21)
# stud3=Student('Sidorov',2203,19)
# stud4=Student('Popov',2203,20)
# stud5=Student('Stepanov',2203,21)

# class Student:
#     def init(self, name='Ivan', age=18, group_number='10A'):# создается метод который вызывается автоматически 
#         # тут создаются базовые параметры 
#         self.name = name
#         self.age = age
#         self.group_number = group_number    
#     def getName(self): # обычный метод которвй придумали мы он просто возвращает имя студента
#         return self.name    
#     def getAge(self): # обычный метод возвращает возрас 
#         return self.age    
#     def getGroupNumber(self):# обычный метод возвращает группу
#         return self.group_number    
#     def setNameAge(self, name, age): # обычный метод , но тут мы уже меняем знаяения 
#         self.name = name
#         self.age = age  
#     def setGroupNumber(self, group_number):
#         self.group_number = group_number
# student1 = Student('William', 20, '11C') # вызывается метод init
# student2 = Student('Jessica', 19, '10A')# вызывается метод init
# student3 = Student('Michael', 21, '10B')# вызывается метод init
# student4 = Student('Cassidy', 18, '9A')# вызывается метод init
# student5 = Student('Elizabeth', 22, '10B')# вызывается метод init
# print(student1.getName(), student1.getAge(),student1.getGroupNumber())
# student1.setNameAge('Dima',000)
# student1.setGroupNumber('11a')
# print(student1.getName(), student1.getAge(),student1.getGroupNumber())

# class Clock:  # вывод времени
#     DAY = 86400  # число секунд в  одном дне
#     def init(self, second) -> None: # при создании
#         self.second = second % self.DAY  # остаток дня
#     def str(self):  # отображать секунды минуты и часы
#         s = self.second % 60  # получение секунд 5
#         m = (self.second//60) % 60  # получение минут 2
#         h = (self.second//3600) % 24  # получение часов   8 (05:12:08)
#         # вывод при помощи классметода
#         return f'{self.get_format(h)}:{self.get_format(m)}:{self.get_format(s)}'
#     @classmethod  # такой метод , который работает только с атрибутами класса
#     def get_format(cls, x):  # возвращает правильный формат времени (00:00:00)  
#         # обычная функция которую придумал я сам так назвал
#         return str(x).rjust(2, '0')  # 03   (16:05:02)
#     def add(self,other): # вызывается при сложении 
#         print(type(self), type(other))
#         if isinstance(other, int): # проверка на то что other ялвяется число
#             return Clock(self.second+other)
#         elif isinstance(other, Clock):# проверка на то что other ялвяется объектом класса
#             return Clock(self.second+other.second)
# s1 = Clock(20000)  # объект
# print(s1) # вызывается метод str
# s1=s1+10000 # вызывается меод add
# print(s1)
# s2=Clock(10000)
# s1=s1+s2 
# print(s1)

# def radd(self,other):
#         print(type(self), type(other))
#         if isinstance(other, int): # проверка на то что other ялвяется число
#             return Clock(self.second+other)
#         elif isinstance(other, Clock):# проверка на то что other ялвяется объектом класса
#             return Clock(self.second+other.second)   
#     def mul(self,other): # при умножении
#         pass
#     def sub(self,other):# при вычитании
#         pass
#     def truediv(self,other):# при делении  x/y
#         pass
#     def floordiv(self, other) :# при делении x//y
#         pass
#     def mod(self, other):# при нахождении остатка x%y
#         pass

# class Fraction:
#     def __init__(self, top=0, bot=1) -> None: 
#         self.top = top
#         self.bot = bot
#     def __str__(self) -> str: # вывод дроби 
#         return f'{self.top}' + f'/{self.bot}' if self.bot != 1 else f''
#     def __add__(self, other):
#         if isinstance(other, Fraction):
#             a = self.top  # числитель 1
#             b = self.bot  # знаменатель 1
#             c = other.top  # числитель 2
#             d = other.bot  # знаменатель 2
#             return Fraction((a*d + b*c), b*d)
#         elif isinstance(other, int):
#             return Fraction((self.top+self.bot*other, self.bot)) 
#     def __sub__(self, other):
#         return self + (other*(-1))
#     def __mul__(self, other):  # умножение
#         if isinstance(other, int):
#             return Fraction(self.top*other, self.bot)
#         elif isinstance(other, Fraction): # дописать щас самим 
#             return Fraction(self.top*other.top,(self.bot*other.bot))          
#     def __truediv__(self, other):# деление 
#         if isinstance(other,int):
#             return Fraction(self.top, self.bot*other)
#         elif isinstance(other,Fraction):
#             return Fraction(self.top*other.bot, self.bot*other.top)       
# a = Fraction(8, 10)
# b = Fraction(6, 10)
# print(a+b, a-b, a/b, a*b)




# import sqlite3

# try:
#     sql_connection=sqlite3.connect('anna.db')
#     cursor = sql_connection.cursor()
#     print('соединение установлено...\nOpen\n')
#     sql_request="""SELECT * FROM anna_table;"""
#     data_list=list(cursor.execute(sql_request))
#     print(data_list)
#     # print('Версия БД...\n', list( cursor.execute(sql_request)))

#     sql_connection.commit()
#     sql_connection.close()
#     print('\nСоединение закрыто...\n/Close')

# except sqlite3.Error as error:
#     print("Ошибка соединения", error)

# finally:
#     if sql_connection:
#         sql_connection.close()

# import sqlite3
# class Db_c:

#     def __init__(self) -> None: # подключаемся к БД 
#         # создание БД и подключение к ней (создаем соединение)
#         self.sql_connection = sqlite3.connect('dima.db')
#         # создаем вспомогательный элемент для запросов к БД
#         self.cursor = self.sql_connection.cursor()
#         print('Соединение установлено...\nOpen\n')

#     def request_version(self): # проверка версии БД
#         sql_request = """select sqlite_version();"""
#         self.cursor.execute(sql_request)
#         print("\nВерсия БД...\n", self.cursor.fetchall())

#     def request_create_table(self): # создание таблицы
#         sql_request = """create table dima_1(id integer primary key, name text not null);       """
#         self.cursor.execute(sql_request)
#         print("\nТаблица создана...\n")

#     def request_insert_values(self): # запись данных в таблицу
#         sql_request = """insert into dima_1(name) values ('qwertyu')"""
#         self.cursor.execute(sql_request)
#         print("\nДанные записаны...\n")

#     def request_select_values(self): # вывод всех данных из таблицы 
#         sql_request = """select * from dima_1"""
#         print("\nДанные из БД...\n", list(self.cursor.execute(sql_request)))

#     def __del__(self): # магический метод который вызывается автоматически при удалении объекта 
#         # когда программа заканчивается то все объекты удаляются чтобы очистить память 
#         # и в этот момент при удалении вызываестя этот метод 
#         # тогда происходит закрытие соединения с БД
#         self.sql_connection.commit()  # сохранение БД
#         self.sql_connection.close()  # закрыть соединение
#         print('\nСоединение закрыто...\nClose')
        


# test= Db_c()
# test.request_version()
# test.request_create_table()
# test.request_insert_values()
# test.request_select_values()