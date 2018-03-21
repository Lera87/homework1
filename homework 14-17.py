import math

#задание 14
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(8))

#if is_even(8):
#     print("The number is even!")
# else:
#     print("The number is odd!")

#задание 15
def cirles_intersects(x1, y1, r1, x2, y2, r2):
    distance_between_centers = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    radius_sum = r1 + r2
    if distance_between_centers > radius_sum:
        return False
    else:
        return True

result = cirles_intersects(3, 4, 5, 14, 18, 8)

if result:
    print('Circles intersect or touch each other')
else:
    print('Circles do not intersect')


#задание 16
def have_trains_crashed(v1, v2):
    total_distance = 10
    first_segment = 4
    second_segment = total_distance - first_segment

    if v1 < v2 * first_segment / second_segment:
        return True
    else:
        return False

#print(have_trains_crashed(50, 108))

if have_trains_crashed(50, 100):
    print("Trains will crash!")
else:
    print("Trains won't crash!")


#задание 17
print("Решение квадратного уравнения (ax ** 2 + bx + c = 0): ")

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return ("Roots are : x1 = {:.2f}, x2 = {:.2f}".format(x1, x2))
    if discriminant == 0:
        x = -b / (2 * a)
        return ("x = {:.2f}".format(x))
    else:
        return ("None roots")

print(solve_quadratic_equation(25, 100, 49))












