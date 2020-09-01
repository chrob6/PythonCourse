# class Rectangle:
#
#     def __init__(self, _a ,_b):
#         self.a = _a
#         self.b = _b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return 2 * self.a + 2 * self.b
#
#     def print_name(selfs):
#         print("Rectangle!!")
#
# rec = Rectangle(2,3)
# rec.a = 2
# rec.b = 2
# print(rec.area())

# class Animal:
#     def __init__(self, _name, _age):
#         self.name = _name
#         self.age = _age
#
#     def introduce(self):
#         print("My name is " + str(self.name) + " and I am: " + str(self.age) + " years old")
#
#     def sound(self):
#         print("Def. sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("woof")
#
# class Cat(Animal):
#     def sound(self):
#         print("Mewn")
#
# ani = Animal("Bruno", 23)
# ani.introduce()
# ani.sound()
#
# doggie = Dog("Doggo", 1)
# doggie.introduce()
# doggie.sound()
#
# cattie = Cat("Cattie", 2.3)
# cattie.introduce()
# cattie.sound()

import time as t
# 1
#a
class snake:
    lenght = 0
    eyes_color = "blank"
    violent = True
    residence = "Earth"

    def attack(self):
        if self.violent:
            return "Aggresive"
        else:
            print("No aggresive!")
            return "-"

    def sound(self):
        print("Zsssssssssss")

    def sleep(self):
        t.sleep(1000)

#b
class fridge:
    capasity = 0
    temperature = 0
    max_freezer_temp = 0
    weight = 0

    def refrigeration(self):
        return self.temperature - 20

    def defrosting(self):
        return self.temperature + 20

    def add_product(self):
        return self.weight + 1
#c
class employee:
    name = "John"
    last_name = "Smith"
    age = 18
    id = 0
    salary = 3000

    def happy_bd(self):
        return self.age + 1

    def increase_salary(self, rise):
        return self.salary + rise

#d
class monster:
    type = "default"
    health = 100
    attack = 1
    defence = 1
    magic = 1

    def fight(self, enemy_def):
        diff = self.attack - enemy_def
        if diff:
            return True
        else:
            return False

    def magic_potion(self):
        self.magic = self.magic + 100

    def change_type(self, decision):
        if decision == 1:
            self.type = "warrior"
        # ...


# 3
# HUMAN
# name, surname, age ,money, position
# __init__, introduce, move, get_position, get_money, say_something, payment, can_buy_beer, buy_beer
#

class Turtle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.x = 0

    def say_name(self):
        print("Hi I am turtle " + self.name)

    def move(self):
        self.x = self.x + self.speed

    def get_position(self):
        return self.x

class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages
        self.current_page = 0

    def print_book(self):
        print(self.title +" written by "+self.author+" has "+str(self.pages)
        +"pages")

    def goto_page(self, page):
        if page < self.pages:
            self.current_page = page
        else:
            self.current_page = self.pages
    def get_current_page(self):
        return self.current_page

# t1 = Turtle("Stefan", 100)
# t2 = Turtle("yerr", 100)
# t2.name = "Yerr"
# t2.speed = 90
# t2.say_name()
# t1.say_name()
# t2.move()
# t1.move()
# print(t2.get_position())
#
# b1 = Book("Rowling", "HP", 1200)
# print(b1.get_current_page())
# b1.goto_page(200)
# print(b1.get_current_page())

class birdy:
    def __init__(self, _weight, _predator, _wing_spread, _speed):
        self.weight = _weight
        self.predator = _predator
        self.wing_spread = _wing_spread
        self.speed = _speed

    def info_list(self):

        print("Spread: " + str(self.wing_spread))
        print("Speed flight: " + str(self.speed))
        print("Weight: " + str(self.weight))
        if self.predator:
            print("Predator: YES")
        else:
            print("Predator: NO")

class ostrich(birdy):
    run_speed = 10

    def info_list(self):

        print("Spread: " + str(self.wing_spread))
        print("Speed run: " + str(self.run_speed))
        print("Speed flight: " + str(self.speed))
        print("Weight: " + str(self.weight))
        if self.predator:
            print("Predator: YES")
        else:
            print("Predator: NO")


# ptok = birdy(20, True, 20, 40)
# strusiok = ostrich(30, False, 34, 37)
# strusiok.run_speed = 12
# ptok.info_list()
# print()
# strusiok.info_list()

#5
import math as m

class figure:
    def __init__(self):
        self.circ_val = -1
        self.area_val = -1
        self.name = "default"

    def area(self):
        return self.area_val

    def circ(self):
        return self.circ_val

    def print_name(self):
        print(self.name)

class triangle(figure):
    def __init__(self, _a, _b, _h):
        super().__init__()
        self.name = "triangle"

        try:
            self.a = float(_a)
            self.b = float(_b)
            self.h = float(_h)
        except ValueError:
            print("Insert good value, You fool!")

    def area(self):
        self.area_val = 1/2 * self.a * self.h
        return self.area_val

    def circ(self):
        self.circ_val = 2* self.b + self.a
        return self.circ_val

class rectangle(figure):
    def __init__(self, _a, _b):
        super().__init__()
        self.name = "rectangle"
        try:
            self.a = float(_a)
            self.b = float(_b)
        except ValueError:
            print("Insert good value, You fool!")


    def area(self):
        self.area_val = self.a * self.b
        return self.area_val

    def circ(self):
        self.circ_val = 2 * self.b + 2 * self.a
        return self.circ_val

class wheel(figure):
    def __init__(self, _r):
        super().__init__()
        self.name = "circle"
        try:
            self.r = float(_r)
        except ValueError:
            print("Insert good value, You fool!")

    def area(self):
        self.area_val = m.pi * self.r * self.r
        return self.area_val

    def circ(self):
        self.circ_val = 2 * m.pi * self.r
        return self.circ_val

# t = triangle(2,2,2)
# r = rectangle(3,3)
# w = wheel(2.3)
# r_wrong = rectangle(2, "siema")
#
# t.print_name()
# print(t.area())
# print(t.circ())
#
# r.print_name()
# print(r.area())
# print(r.circ())
#
# w.print_name()
# print(w.area())
# print(w.circ())