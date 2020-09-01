import random as r
class Human:
    def __init__(self, name, surname, age, money, position):
        self.name = name
        self.surname = surname
        self.age = age
        self.money = money
        self.position = position

    def introduce(self):
        print("Hi I am " + self.name + " " + self.surname)

    def move(self, distance):
        self.position = self.position + distance

    def get_position(self):
        return self.position

    def get_money(self):
        return self.money

    def say_something(self, something):
        print(something)

    def payment(self, salary):
        self.money = self.money + salary

    def can_buy_beer(self, count, price):
        if self.age >= 18 and self.money >= count * price:
            return True
        else:
            return False

    def buy_beer(self, count, price):
        if self.can_buy_beer(count, price):
            self.money = self.money - count * price
            print("Great! "+self.name+" bought "+str(count)+" beers!")
        else:
            print("Not possible for this human!")

zbyszek = Human("Zbyszek", "Lewandowski", 45, 50000, r.randint(25,29))
heniek = Human("Heniek", "Brzeczek", 20, 10, 3)

heniek.buy_beer(3, 5)
destination = zbyszek.get_position()

while True:
    heniek.move(1)
    distance = abs(heniek.get_position() - zbyszek.get_position())
    if not distance:
        break
    if heniek.get_position() % 2 == 0:
        heniek.say_something(str(distance) + " houses remaining to that thief!")

heniek.introduce()
heniek.payment(500)
zbyszek.payment(-500)
zbyszek.say_something("Oh no! He'll ruin me, I have only " + str(zbyszek.get_money()) + " zl right now!")

heniek.position = 15
heniek.buy_beer(6, 5)




