# zajecia nr 1
# my_list = []
# for i in range (6):
#     if (i % 2 == 0):
#         my_list.append(i+1)
# print(my_list)
#
# my_list_py = [ i+1 for i in range(6)]
# print(my_list_py)

# my_list_sq = [i*i if i%2==0 else 0 for i in range(1,11)]
# print(my_list_sq)
# my_list = []
# for a in [8,10,15,19,25]:
#     if a // 3 >= 5:
#         my_list.append(a+2)
# print(my_list)
#
# dwa = [a+2 for a in [8,10,15,19,25] if a // 3 >= 5]
# print(dwa)
# uje_kwadrat = [-i*i if i % 2==1 else "haha" for i in range(5,21)]
# print(uje_kwadrat)
# import matplotlib.pyplot as plt
# import random as r
# import math as m
# numbers = [5,10,15,3,20]
# # plt.plot(numbers, 'mp--') #dużo wariantów /o,s,*,-,D,p - pierwsz literka kolor
# # plt.show()
# #y = 5x - 2
# X = [i +1 for i in range (0,10)]
# Y = [5*x-2 for x in X]
#
# plt.axhline()
# plt.axvline()
# plt.plot(X,Y,'ro--')
# plt.xlabel("OX")
# plt.ylabel("OY")
# plt.title("wykres")
# plt.show()
# import matplotlib.pyplot as plt
# import random as r
#
# names = ["Ania","Kasia", "Pawl","Olga","stefan"]
# ages = [r.randint(18,100) for name in names]
# print(ages)
# plt.bar(names, ages, color=['red', 'green', 'blue'])
# plt.xticks()
# plt.yticks()
# plt.show()

# e = ["mieszkanie", "media","jedzienie","rozrywka","nauka","inwestycja"]
# p = [2200, 300, 800, 1000, 300,200]
#
# explode = [0 for i in e] # tablica zer o rozmiarze e
# explode [e.index("inwestycja")] = 0.1
# plt.pie(p,
#         labels = e,
#         explode = explode,
#         autopct = "%.2f %%",
#         shadow=True)
#
# plt.axis('equal')
# plt.show()

# X = [x for x in range(0,360+1,10)]
# Y1 = [m.cos(m.radians(i)) for i in X]
# Y2 = [r.random() for i in X]
#
# #plt.subplot(1,2,1)
# plt.subplot(2,1,1)
# plt.plot(X,Y1, "r.-")
# #plt.subplot(1,2,2)
# plt.subplot(2,1,2)
# plt.plot(X,Y2, "bs:")
# plt.show()


import math as m
import random as r
import csv
import matplotlib.pyplot as plt
import numpy as np

#zad1.1
# #a 1 4 27 256
# print([x**x for x in [1,2,3,4]])
# #b nope 5.5 nope 6.5 nope 7.5
# print([x/2 if x%2 else "Nope" for x in range(10,16)] )

#zad1.2

# my_list = []
# #a my_list = [x**3 for x in range(1,11)]
# #b my_list = [ord(x) for x in 'Marcin']
# my_list3c = [m.sin(m.radians(x)) for x in range(0,361,10)]
# #d my_list = [len(x) for x in ["Kacper","Konrad","Krystian","Klaudia","Mateusz"]]
# #e my_list = [x*2 for x in range(3,50,3)]
# my_list3f = [r.random() if x%2 == 0 else -r.random() for x in range(0,100)]
# print(my_list)

#zad1.3
# X_zero_hundred = [x for x in range(0,100)]
# X_zero_ten = [x for x in range(0,11)]
# X_mten_ten = [x for x in range(-10,11)]
# X_sin = [x for x in range(0,361,10)]
# Y1 = [2*x + 5 for x in X_zero_ten]
# Y2 = [x**2 - 2*x - 8 for x in X_mten_ten ]
#
# plt.subplot(2,2,1)
# plt.plot(X_zero_ten, Y1,"r*")
# plt.subplot(2,2,2)
# plt.plot(X_mten_ten, Y2,"m:")
#
# plt.subplot(2,2,3)
# plt.plot(X_sin, my_list3c,"bp--")
# plt.subplot(2,2,4)
# plt.plot(X_zero_hundred, my_list3f,"g^--")
# plt.show()

#zad1.4
# activities = {"sen":6, "praca":8, "transport":1, "jedzenie":1, "mecz":2, "nauka":2, "piwo":1, "serial":1, "higiena":2}
# plt.pie(activities.values(), labels=activities.keys(),
#         autopct="%.2f %%",
#         shadow=True
#         )
# #plt.axis('equal')
# plt.show()

#zad1.5
# A = 50
# freq = [x for x in range (100,10001,5)]
# v = [A + r.choice([-1,1]) for x in freq]
# plt.plot(freq,v)
# plt.ylim(20,70)
# plt.show()




