
import math

def circle(r):
    return math.pi * r**2

def rectangle(a, b):
    return a*b

def triangle(a, b, c):
    p = (a+b+c)/2
    return math.sqrt(p * (p-a) * (p-b) * (p-c))

choice = input("Circle(c), Rectangle(r) or Triangle(t): ")
if choice == 'c':
    rad = float(input("Radius: "))
    print("Area of a Cirlce: %.2f" % circle(rad))
elif choice == 'r':
    l = float(input("Length: "))
    w = float(input("Width: "))
    print("Area of a Rectangle: %.2f" % rectangle(l,w))
elif choice == 't':
    AB = float(input("First side: "))
    BC = float(input("Second side: "))
    CA = float(input("Third side: "))
    print("Area of Triangle: %.2f" % triangle(AB,BC,CA))
