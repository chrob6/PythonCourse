import random as r

elements = []
N = int(input("How many elements: "))
for i in range(N):
    elements.append(r.random())
elements = sorted(elements)

with open("percent.txt", "w") as f:
    for i in elements:
        to_write = str(i) + " ; " + str(int(round(i * 100, 0))) + "%" + "\n"
        f.write(to_write)
