import math

#11задание
def degrees2radians(degrees):
    formula_degrees2radians = degrees * math.pi / 180
    return formula_degrees2radians

print("Косинус угла 45 градусов равен : %.4f" % (math.cos(degrees2radians(45))))
print("Косинус угла 40 градусов равен : %.4f" % (math.cos(degrees2radians(40))))
print("Косинус угла 60 градусов равен : %.4f" % (math.cos(degrees2radians(60))))

#13задание
def triangle_square_and_perimeter(a, b):
    triangle_square = a * b / 2
    c = math.sqrt(a**2 + b**2)
    perimeter = a + b + c
    return triangle_square, perimeter

res1, res2 = triangle_square_and_perimeter(8,5)
print("Площадь треугольника : %.2f, а его периметр : %.2f" % (res1, res2))

#12задание
input_number = input('Enter a 3 digit number: ')

def sum_of_digits(number):
    str_number = str(number)
    total = int(str_number[0]) + int(str_number[1]) + int(str_number[2])
    return total

print(sum_of_digits(input_number))

