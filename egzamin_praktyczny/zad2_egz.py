numbers = []
print_numbers = True
while 1:
    try:
        n = input("Gimme number: ")
        if n == "exit":
            break
        n = float(n)
        numbers.append(n)
    except ValueError:
        print("Podałeś " + str(len(numbers)) + " liczb. Dalej się nie bawię")
        print_numbers = False
        break

if print_numbers:
    for i in numbers:
        if i == int(i):
            i = int(i)
        print(i)
