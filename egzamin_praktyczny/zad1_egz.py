import math as m


def circle_area(r):
    return m.pi * r * r


def triangle_area(a, h):
    return (1 / 2) * a * h


def rectangle_area(a, *b):
    if b:
        return a * b[0]
    else:
        return a * a


while 1:
    print("Area of: ")
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. - Quit program")
    decision = input("Choose numer to calculate area: ")

    try:
        if decision == '1':
            figure = "Koło"
            r = float(input("Insert r(radius): "))
            area = circle_area(r)

        elif decision == '2':
            figure = "Trójkąt"
            a = float(input("Insert a(one side of the triangle): "))
            h = float(input("Insert h(height): "))
            area = triangle_area(a, h)

        elif decision == '3':
            a = float(input("Insert a(first side): "))
            b = float(input("Insert b(second side): "))
            if a == b:
                figure = "Kwadrat"
                area = rectangle_area(a)
            else:
                figure = "Prostokąt"
                area = rectangle_area(a, b)
        elif decision == '4':
            break
        else:
            print("Wrong input!")
            print()
            continue

    except ValueError:
        print("Insert a number value!")
        print()
        continue

    try:
        print("Pole figury " + figure + " o podanych wartościach wynosi " + str(
            area))  # Po polsku bo tego wymagało polecenie
        print()
        figure, area = "", ""
    except NameError:
        print("Unable to print final statement")
        print()