class Shape:
    def circle(self, side):
        print("Circle")
        print("Area: ", 3.14*side*side)
        print("Perimeter: ", 2*3.14*side)

    def rectangle(self, side1, side2):
        print("Rectangle")
        print("Area: ", side1*side2)
        print("Perimeter: ", 2*side1*side2)

    def triangle(self, side1, side2, side3):
        print("Triangle")
        print("Area: ", (side1*side2)*side3)
        print("Perimeter: ", side1+side2+side3)


class Client(Shape):
    def __init__(self, ch):
        if ch == 1:
            self.side = int(input("Enter side: "))
            Shape.circle(self, self.side)
        elif ch == 2:
            self.side1 = int(input("Enter side1: "))
            self.side2 = int(input("Enter side2: "))
            Shape.rectangle(self, self.side1, self.side2)
        elif ch == 3:
            self.side1 = int(input("Enter side1: "))
            self.side2 = int(input("Enter side2: "))
            self.side3 = int(input("Enter side3: "))
            Shape.triangle(self, self.side1, self.side2, self.side3)


print("1.Circle\n2.Rectangle\n3.Triangle")
choice = int(input("Enter your choice:"))
client = Client(choice)

