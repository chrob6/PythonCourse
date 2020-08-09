shoppings = input("Insert your shopping list divided by ',' :")
shoppings = shoppings.split(",")
shoppings = set(shoppings)
dict_shoppings = {}
credit = 100  # 100zl
full_price = 0
print(shoppings)
for i in shoppings:
    try:
        price = float(input("How much for " + i + ": "))
    except ValueError:
        price = 0
    i = i.upper()
    dict_shoppings[i] = price

for i in dict_shoppings.values():
    full_price = full_price + i

if credit >= full_price:
    print("Enough money, you can buy this products.")
else:
    print("Not enough money, you can NOT buy this products.")