"""
Создать класс MobilePhone на основе класса Phone из пред ДЗ, у которого будут следующие атрибуты:
добавить свойства:
	is_busy - занято - когда кто-то позвонил до момента когда положили трубку должен иметь значение True
переопределить методы:
	- receive_call - теперь не только выводит фразу с именем но и сохраняет время и имя в историю.
						Если в момент вызова трубка еще не положена - вернуть "занято".
добавить методы:
		- receive_sms - принимает имя и текст и сохраяет в историю
		- call_history - возвращает историю звонивших с датой и временем именем и случайным номером телефона формата +375*********
		- sms_histiry - возвращает историю sms (имя/дата/время/текст)
		- сделать метод (положил трубку)
		* метод receive_call принимает номер и если есть в справочнике в историю записать имя
		* положить трубку с возвратом  времени разговора которое тоже в записывается историю
"""
import datetime
import random

class Phone:
    brand: str
    model: str
    issue_year: int
    call_history: list
    sms_history: list

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.call_history = []
        self.sms_history = []


    def get_info(self):
        print(f"{self.brand} {self.model} {self.issue_year}\nCall history:\n{self.call_history}\n")


    def receive_call(self, name, tel):
        self.name = name
        self.tel = tel
        self.call_history.append(["18.04.2022", "15:45", name, tel])
        print(f"{name} is calling, Phone number +{tel}\n")
        return " "

Доделать!
   # def view_call_history(self):
     #   for i in self.call_history:



    def receive_sms(self, name, tel, text):
        self.name = name
        self.tel = tel
        self.text = text
        self.sms_history.append([name, tel, text])
        print(f"{name} (+{tel}) send sms. Text:\n{text}\n\n")
        return " "

phone1 = Phone("iPhone", "13 Pro", 2021)

#phone2 = Phone("Samsung", "21 lite", 2020)
#phone2.get_info()

phone1.receive_call ("Dan", random.randint(3751000000, 3759999999))
time.sleep(1)
phone1.receive_sms ("Dan", random.randint(3751000000, 3759999999), "Hi, How are you?")
time.sleep(1)
phone1.receive_sms ("Alex", random.randint(3751000000, 3759999999), "Call me")
time.sleep(1)

phone1.get_info()

