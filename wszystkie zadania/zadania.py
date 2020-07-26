# #zad1.1
# print("Marcin")
# print("Chrobak")
# print('"Harry Potter and the Deathly Hollows"')
# #zad1.2
# age = int(input("Insert age"))
# print(2020-age)
# #zad1.3
# print(int(100/33))
# print(100//33)
# #zad1.4
# a = 4
# b = 9
# r1 = 12
# r2 = 13
# if r1 > r2:
#     h = r2
# elif r1 <= r2:
#     h = r1
#
# area = h*(a+b) / 2
# print(area)
# #zad1.5
# print("wynik działania to: " +str(55*66*77-3))
########
#2.1
# age = int(input("Insert age"))
# print("Nice your age is "+str(age))
# print("In one year time your age will be: " +  str(age+1))
# #2.2
# x = int(input("Frist: "))
# y = int(input("Sec: "))
# print("Sum: " + str(x+y))
# print("Difference: " + str(x-y))
# print("Multiply: " + str(x*y))
# if y != 0:
#     print("Divide: " + str(x/y))
#2.3
# number = input("Insert any number: ")
# intnumber = int(number)
# access = isinstance(intnumber, int)
# if access:
#     if number % 2 == 0:
#         print("even")
#     else:
#         print("uneven")
#2.4
# age = int(input("Your age: "))
# money = int(input("How much money do you have?: "))
#
# if money >= 20 and age > 17:
#     print("Let's buy vodka!")
# elif money >= 20 and age < 17:
#     print("Rich but too young")
# elif money <= 20 and age > 17:
#     print("Poor little old man")
# else:
#     print("too poor, too young")
#2.5
# val = 10/3 # -10/3 , 10//3
# if val > 3:
#     print("big")
# elif val == 3:
#     print("middle")
# else:
#     print("small")
#2.6
# dec = int(input("Your 1. Monthly or 2. Annual income "))
# income = int(input("Your income: "))
#
# if dec == 1:
#     income = income*12
#
# if income < 85252:
#     print("First: " + str(income*0.17))
# else:
#     print("Sec: " + str(income*0.32))
# friends = ["Wacper", "Crystian", "Aonrad","Mateusz"]
# sort_friends = sorted(friends)
# print(sort_friends)


# LISTA
# my_list = [11,12,13]
# my_list[1] = 15
# print(my_list)
# my_list.append(23)
# print(my_list)
# my_list.insert(1, 12)
# print(my_list)
# x = my_list.pop()
# print(x)
# print(my_list)
# my_list.reverse()
# print(my_list)
#
# my_list2 = [100,200]
# list = my_list + my_list2
# print(list)
# mul_list = my_list * 4
# print(mul_list)
# print(mul_list[:3])
# print(mul_list[4:9])
# print(mul_list[9:])
# print(mul_list[0:10:2])

# TUPLE
# tuple = (2,34,5,2) #można bez nawiasow
# print(tuple)

# DICT - w innych jezykach mapa
# my_dict = { "apples": 5, "bananas": 4, "cherries": 3}
# # print(my_dict)
# # print(my_dict["apples"])
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
#
# print(sum(my_dict.values()))
#
# my_dict.update( {"melon":2})
# print(my_dict)
# print(my_dict["melon"])
# del my_dict["cherries"]
# my_dict["bananas"] = 44
# print(my_dict)

# Set - nieuporzadkowane elementy, bez powtórzen

# my_set = { 1,2,3,4,5}
# print(my_set)
# my_set.add(7)
# print(my_set)
# my_set.remove(2)
# print(my_set)
# x = my_set.pop()
# print(x)
# print(3 in my_set)

#string
# name = "Marcinek"
# print(name)
# print(name[0])
# print(name[1:4])
# print(name.find("cin"))
# print(name.find("x"))
# print(name.replace("ek", ""))
# print(name)
# print(name.upper())
# print(name.lower())
# print("a.b.c".split("."))
# print("".join(["a","b","c"]))

#lista
# x = []
# x = list()
# #krotka
# x = ()
# x = tuple()
# # slownik
# x = {}
# x = dict()
# # zbior
# x = set()

# print(list("alfabet"))
# print("napis"+str([1,2,3]))
# print(list({1,5,6,7}))
# print(set("alfabet"))
# print(set([1,2,4,1,2,1,3,4,1]))

# for i in range(1,11):
#     print(i)
#
# tab = [2,3,4,5,6]
# for i in tab:
#     print(i)
#
# list = [1,5,10,15,20]
# for i in list:
#     print(i*i)

# val = 3
# while val:
#     if val > 1000:
#         break;
#     val = val+5
#     print(val)

# for i in range(0,100):
#     if i % 2 == 1:
#         continue
#     print(i)

# for x in range(8):
#     for y in range(6):
#         print("Piksel: " + str(x) + ", " + str(y) )

# grass = "."
# enemy = "x"
# coin = "*"
# river = "="
# x = 0
# y = 0
# p = " "
#
# for j in range(5):
#     x = 0
#     for i in range(6):
#         p = grass
#         if (x == 2 and y == 0) or (x == 1 and y == 1) or (x == 3 and y == 3) or (x == 5 and y == 3):
#             p = coin
#         if (x == 0 and y == 1) or (x == 2 and y == 3) or (x == 2 and y == 4) or (x == 3 and y == 4):
#             p = enemy
#         if y == 2:
#             p = river
#         print(p, end=" ")
#         x = x+1
#     print(p)
#     y = y+1

#zad3.1
# tab = [5, 15, 1, 25, 2]
# tab_t = sorted(tab, reverse = True)
# tab_f = sorted(tab, reverse = False)
# print(tab_t)
# print(tab_f)

# x = 1,2,3,4
# print(type(x))

#zad3.3 zad4.7 zad6.6
# import calendar
# import datetime
# dict_bill = {2: 2300, 3:2100, 4:1800, 5:3000, 7: 2900, 8: 1000, 1:2000,}
# #dict_bill = {"luty": 2300, "marzec":2100, "kwiecien":1800,"maj":3000,"lipiec": 2900,"sierpien": 1000}
# print("Min: " + str(min(dict_bill.values())))
# print("Min: " + str(max(dict_bill.values())))
# print("Suma: " + str(sum(dict_bill.values())))
# avg = sum(dict_bill.values())/len(dict_bill)
# print("Avg: " + str(avg))
# x = dict_bill.keys()
# sx = sorted(x)
# if avg > dict_bill[sx[-1]]:
#     print("Start save money!")
# else:
#     print("you good")
#
# for i in dict_bill:
#     if dict_bill[i] > avg:
#         print(str(datetime.date(1,i,1).strftime('%B')) + ":" + str(dict_bill[i]))
#

#time.strftime("%B", time.struct_time((0, mn, 0,) + (0,) * 6))

#zad3.4 zad4.8
# randomize = input("podaj 5 liczb oddzielonymi przecinkiem:")
# randomize_list = randomize.split(",")
#
# j = 0
# for i in randomize_list:
#     randomize_list[j] = int(i)
#     j = j+1
# print(randomize_list)
#
# if len(randomize_list) == 5:
#     randomize_set = set(randomize_list)
#     x = randomize_set.pop()
#     if max(randomize_list) == x:
#         print("The largest")
#     if min(randomize_list) == x:
#         print("The smallest")
#     print("Randomized: " + str(x))


#zad4.2
#for i in range(0,13,3):
#    print(i)
# a = 3
# while a != -4:
#     print(a)
#     a = a-1

#zad4.3
# tabx = [1,3,5,7]
# taby = [2,4,6]
# for x in tabx:
#     for y in taby:
#         if (x != 3 and y != 2):
#             print(str(x) + "," + str(y))

#zad4.4
#..

#zad4.5
# dict_products = {}
# products = input("Podaj produkty oddzielonych przecinki: ")
# seperate_products = products.split(",")
# set_products = set(seperate_products)
# numberofproducts = len(set_products)
#
# for i in set_products:
#     price = int(input("Cena dla " + i + ": "))
#     dict_products[i] = price
#
# for i in dict_products:
#     print(i + ":" + str(dict_products[i]))

#zad4.6
# test = 1
# while True:
#     print(test)
#     if test < 0:
#         break
#     test = test - 1

#zad4.7

#for ambition ones
# lvl = int(input("Level of triange: "))
# lvl_ptr = 1
#
# while lvl_ptr <= lvl:
#     if lvl_ptr == 1:
#         print("1".center(lvl))
#     if lvl_ptr == 2:
#         print("1 1".center(lvl))
#     if lvl_ptr > 2:
#         print(str(1).center(lvl), end=" ")
#         print(str(2).center(lvl), end=" ")
#         print(str(1).center(lvl), end=" ")
#     lvl_ptr = lvl_ptr + 1

# def write_list(list):
#     print(' '.join([str(item) for item in list]).center(30))
#
# x = input("Podaj liczbe poziomow: ")
# line = [1]
# write_list(line)
# for i in range(int(x) - 1):
#     next_line = [1]
#     for j in range(len(line) - 1):
#         next_line.append(line[j] + line[j + 1])
#     next_line.append(1)
#     line = next_line
#     write_list(line)
#
# lista = ['2','3','4','5','6','1','2','4','5']
# print([int(item) for item in lista])

#cw5.1
# def wheel_area(r):
#     return 3.14 * r * r
# print(wheel_area(2))

#cw5.2
# def trapeze_area(a,b,h):
#     return (1/2) * (a + b) * h
# print(trapeze_area(1,4,2))

#cw5.3
# def no_positive(x):
#     if x > 0:
#         print("Greater than 0")
# no_positive(0)

#cw5.4
# def programista(name , age):
#     print(name + " siedzi obok mnie i ma " + str(age))
# programista("Marcin", 21)
# programista("Matuesz", 22)

#cw5.5
# def base_area(a, b):
#     return a * b
# def volume(p,h):
#     return p*h
# print(volume(base_area(2,2), 2))

#cw5.6
# def fun(first, sec, *optional):
#     return [first, sec] + list(optional)
# print(fun(1,2,4,5,6,7,8,9,0))

#zad5.1
# def compare(a,b,c):
#     if a > b and b < c:
#         return 3
#     elif a < b and c == 3:
#         return 5
#     elif a <= b and c > 1:
#         return 10
#     else:
#         return 99
#
# print(compare(3,1,2)) # 3
# print(compare(3,2,1)) # 99
# print(compare(3,3,3)) # 10
# print(compare(1,2,3)) # 5
# print(compare(3,2,3)) # 3
# print(compare(1,1,1)) # 99

#zad5.2
# def dodaj(a,b,c):
#     return a + b + c
# print(dodaj(1,2,3))

#zad5.3
# def get_value(aaa):
#     return aaa
# print(get_value("siema"))

#zad5.4
# def calculator(sign, a, b):
#     if sign == "+":
#         return a + b
#     if sign == "/":
#         return a / b
#     if sign == "-":
#         return a - b
#     if sign == "*":
#         return a * b
#
# sign = input("Choose calculation(+, /, *, -): ")
# a = float(input("First number: "))
# b = float(input("Second number: "))
# print(calculator(sign, a, b))

#zad5.5
# def man_or_woman(name):
#     if name[-1] == "a":
#         return "woman"
#     else:
#         return "man"
#
# name_list = ["Marcin", "Karina", "Kacper", "Krystian", "Mateusz"]
# name_dict = {}
# for i in name_list:
#     name_dict[i] = man_or_woman(i)
# print(name_dict.items())

#zad5.6 zad7.5
# def trapeze_area(a,b,h):
#     return 1/2 * (a + b) * h
# def triangle_area(a,b,c):
#     if a+b <= c or b+c <= a or c+a <= b:
#         return 'blad'
#     p = 1/2*(a+b+c)
#     return pow(p*(p-a)*(p-b)*(p-c), 1/2)
# def squere_fun(a,b,c):
#     if a == 0:
#         return "blad"
#     d = b*b - 4*a*c
#     if d > 0:
#         x1 = (-b - pow(d,1/2))/ 2 * a
#         x2 = (-b + pow(d,1/2)) / 2 * a
#         ret = (a,b)
#         return ret
#     if d == 0:
#         return -b/2*a
#     if d < 0:
#         return "brak"
#
# try:
#     # first = input("First number(a): ")
#     # sec = input("Second number(b): ")
#     # third = input("Third number(c or h): ")
#     first = float(input("First number(a): "))
#     sec = float(input("Second number(b): "))
#     third = float(input("Third number(c or h): "))
# except ValueError:
#     print("Insert a number, you fool")
#
# try:
#     print(trapeze_area(first,sec,third))
#     print(triangle_area(first,sec,third))
#     print(squere_fun(first,sec,third))
# except NameError:
#     print("That's why you can not invoke function, you fool")
#zad5.7
# def fun_itr(x):
#     for i in range(x+1):
#         for j in range(i):
#             print("*", end="")
#         print()
#
# def fun_rek(x): NIE WIEM
#     print("*", end="")
#     if x > 0:
#         print()
#         print("*")
#         fun_rek(x-1)
#fun_rek(4)

#zad5.8
# def fib(x):
#     if x < 1:
#         return 0
#     if x < 2:
#         return 1
#     return fib(x-1) + fib(x-2)
#
# print(fib(9))

#zad6.1
# import random
# my_list = [1,2,3]
# random.shuffle(my_list)
# print(my_list)

#zad6.2
# import random
# geo_avg = 1
# pre_krotka = []
# a = int(input("Start range: "))
# b = int(input("Finish range: "))
# for i in range(10):
#     rand = random.randint(a,b)
#     geo_avg = geo_avg*rand
#     pre_krotka.append(rand)
#
# krotka = tuple(pre_krotka)
# print(krotka)
# geo_avg = pow(geo_avg,(1/len(krotka)))
# print(geo_avg)

#zad6.3
# import math as m
# a = int(input("podaj a: "))
# b = int(input("podaj b: "))
# alfa = int(input("podaj alfa: "))
#
# if alfa < 90:
#     p = (1/2)*a*b*m.sin(m.radians(alfa))
#     print(p)
# else:
#     print("zly kat")

#zad6.4
# import random as r
# while 1:
#     a = int(input("Start range: "))
#     b = int(input("Finish range: "))
#     if b-a < 15:
#         print("Za maly przedzial")
#     else:
#         break
# rand = r.randint(a,b)
# chances = 3
# number_ch = 0
# while number_ch < chances:
#     shot = int(input("Strzał: "))
#     if rand < shot:
#         print("Za duzo!")
#     elif rand > shot:
#         print("Za malo!")
#     elif rand == shot:
#         print("WYGRALES!")
#         break
#     chances = chances - 1
#     print("Zostało prób: " + str(chances))

#zad6.5
# import datetime
# import time
# year = int(input("year: "))
# mth = int(input("month: "))
# day = int(input("days: "))
# given = datetime.date(year,mth,day)
# twoafter = given + datetime.timedelta(weeks=2)
# twobefore = given - datetime.timedelta(weeks=2)
# print(twoafter)
# print(twobefore)
# firstday = datetime.date(year,1,1)
# numberofdays = given - firstday
# print(numberofdays)
# print(numberofdays.days//7)
# days_to_sunday = 6-given.weekday()
# next_sunday = given + datetime.timedelta(days=days_to_sunday)
# print(next_sunday)

#zad6.6 ..

#zad6 for ambitions
# import random as r
# import time as t
#
# def print_list(list_):
#     for i in list_:
#         print(i, end ="")
#     print()
#
# def init_alfabet():
#     alfabet = ""
#     for i in range(97, 123):
#         alfabet = alfabet + chr(i)
#     return alfabet
#
# def init_word_to_guess(word):
#     to_guess = list(word)
#     i = 0
#     while i < len(word):
#         to_guess[i] = '_'
#         i = i + 1
#     print("You've to guess this word: ", end="")
#     print_list(to_guess)
#     print()
#     return to_guess
#
# s_word = input("Insert word to hang s'one: ")
# s_word = s_word.lower()
# l_word = list(s_word)
# temp_word = s_word
#
# alfabet = init_alfabet()
# to_guess = init_word_to_guess(s_word)
# chances = 0
#
# while chances < 10:
#     while 1:
#         chosen = r.choice(alfabet)
#         if chosen == '_':
#             continue
#         else:
#             alfabet = alfabet.replace(chosen, "_")
#             break
#     print("Chosen letter: " + chosen)
#
#     while 1:
#         change = temp_word.find(chosen)
#         if change > -1:
#             to_guess.remove("_")
#             to_guess.insert(change,chosen)
#             temp_word = temp_word.replace(temp_word[change], "!")
#         else:
#             break
#
#     print_list(to_guess)
#     print(alfabet)
#     print("Round" + str(chances+1) + "/10")
#     print()
#     win_checker = 0
#     for i in to_guess:
#         if i != '_':
#             win_checker = win_checker + 1
#     if win_checker == len(to_guess):
#         print("YOU WON")
#         break
#
#     chances = chances + 1
#     if chances == 10:
#         print("  |--------|")
#         print("  |        |")
#         print("  O        |")
#         print(" /|\       |")
#         print("  |        |")
#         print(" / \       |")
#         print("           |")
#         print("      ----------")
#     t.sleep(1)

#7.operacje na plikach
# my_file = open("test.txt","r")
# #print(my_file.read())
# # print(my_file.read(5))
# # print(my_file.read(5))
# # for i in range(3):
# #     print(my_file.readline())
# # list_of_lines = my_file.readlines()
# # print(list_of_lines)
# # print(list_of_lines[1].strip())
#
# my_file.close()
# for i in range (-5,5):
#     try:
#         print(10/i)
#     except ZeroDivisionError:
#         print("Cholero!")
#     finally:elo
#         print("good")
# num = input("Number pls: ")
# try:
#     num = float(num)
# except ValueError:
#     num = 0
# finally:
#     print(num*num)

# def square_area(a):
#     if a <= 0:
#         raise ValueError
#     return a*a
#
# try:
#     print(square_area(5))
#     print(square_area(-5))
# except ValueError:
#     print("Debil matematyczny")

#zad7.1
# import random as r
# a = int(input("Start range: "))
# b = int(input("End range: "))
# rand = []
# for i in range(10):
#     ra = r.randint(a,b)
#     rand.append(ra)
#
# with open("f.txt", "w") as f:
#     for i in rand:
#         for j in range(i):
#             f.write("*")
#         f.write("\n")
#
# # with open("f.txt","r") as f:
# #     print(f.read())
#
# dots = ""
# dot = "."
# end = "\n"
# for i in rand:
#     for j in range(i):
#         #print(dot,end="")
#         dots = dots + dot
#     #print()
#     dots = dots + end
#
# print()
# with open("f.txt","r") as f:
#      dots = f.read() + dots
#      print(dots)

#zad7.2
# import random as r
# students = ["Rostenkowski","Cooper","Hoofstader","Holowitz","Kootrophali","Cooper","Cooper","Holowitz"]
# grades = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
# students_count = []
# marks = {}
#
# for i in students:
#     students_count.append(students.count(i))
#
# for i in range(len(students)):
#     if students_count[i] == 1:
#         pass
#     elif students_count[i] > 1:
#         while students_count[i] > 0:
#             for j in range(len(students)-1,0,-1):
#                 if students[i] == students[j]:
#                     students[j] = students[j] + str(students_count[i])
#                     students_count[i] = students_count[i] - 1
#
#
#
# # for i in students_count:
# #      print(students_count)
#
# for i in range(len(students)):
#     marks[students[i]] = r.choice(grades)
#
# with open("students.txt","w") as f:
#     for i in range(len(marks)):
#         to_file = str(i+1) + ". " + str(students[i]) + " : " + str(marks[students[i]]) + "\n"
#         f.write(to_file)
#
# with open("students.txt", "r") as f:
#     print(f.read())

#zad7.3
# import csv
# with open('kody.csv', 'r') as f:
#     f.read()

#zad7.4
#a
# my_list = [1,2,3]
# try:
#     x = my_list[5]
# except IndexError:
#     print("Out of range")
#b.
# my_dict = {"apples": 3, "bananas":5, "oranges": 9}
# try:
#     print(my_dict["cherries"])
# except KeyError:
#     print("Bad key")
#c.
# try:
#     print("Zmyslow" + 5)
# except TypeError:
#     print("Bad Type")
#d.
# try:
#     import maths
# except ModuleNotFoundError:
#     print("There is not any module like that")
#e.
# try:
#     x = 1
#     y = 2
#     z = w
# except NameError:
#     print("Define!")

#zad7.5


















