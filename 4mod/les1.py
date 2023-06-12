# class Solution:
#     def hello(self, name = 'Ivan', fam = 'Ivanov', age = 14):
#         self.name = name
#         self.fam = fam
#         self.age = age
#         print(f'Hello {name} {fam} {age} years old')
# a=Solution()
# a.hello('Dima', 'Petrov', 20)
# a.hello('Dima', 'Petrov')
# a.hello('Dima')
# a.hello()
# class Solution2(Solution):
#     def hello(self, age):
#         if age>=18:
#             print("Привет, ты совершеннолетний/яя")
#         else:
#              print("Привет, ты несовершеннолетний/яя")
# Masha = Solution2()
# Masha.hello(19)

# from kivy.app import App
# from kivy.uix.label import Label
# class MainApp(App):
#     def build(self):
#         label = Label(text='Привет, мир!')
#         return label
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()

# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# class MainApp(App):
#     def build(self):
#         layout = BoxLayout()
#         label1 = Label(text='Привет')
#         label2 = Label(text='мир')
#         layout.add_widget(label1)
#         layout.add_widget(label2)
#         return layout
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()

# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# class MainWidget(BoxLayout):
#     pass
# class Main1App(App):
#     def build(self):
#         return MainWidget()
# if __name__ == '__main__':
#     app = Main1App()
#     app.run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
class MainWidget(BoxLayout):
    hello_label = ObjectProperty()
    name_input = ObjectProperty()
    name_input1 = ObjectProperty()
    def say_hello(self):
        self.hello_label.text = str(int(self.name_input.text)* int(self.name_input1.text))
class Main2App(App):
    def build(self):
        return MainWidget()
if __name__ == '__main__':
    app = Main2App()
    app.run()