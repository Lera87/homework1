#print(42)
import math

length = 10
width = 20
rectangle_square = length * width
print("Площадь прямоугольника при ширине %d см. и длине %d см. равна: %d кв. см." % (width, length, rectangle_square))

catheter1 = 4
catheter2 = 4
hypotenuse = math.sqrt(catheter1**2 + catheter2**2)
#hypotenuse = (catheter1**2 + catheter2**2)**0.5
print("Гипотенуза при катете1 %d и катете2 %d равна: %.2f" % (catheter1, catheter2, hypotenuse))

#площадь круга
radius = 42
circle_square = math.pi * (radius**2)
print("При радиусе %.2f площадь круга равна %.2f" % (radius, circle_square))