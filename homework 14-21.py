import math
import random

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


print("----------------------------------------")


#задание 15
def circles_intersects(x1, y1, r1, x2, y2, r2):
    distance_between_centers = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if distance_between_centers == r1 + r2 or distance_between_centers == abs(r1 - r2):
        return True
    elif distance_between_centers < r1 + r2 and distance_between_centers > abs(r1 - r2):
        return True
    elif distance_between_centers > r1 + r2 or distance_between_centers < abs(r1 - r2):
        return False

print(circles_intersects(3, 4, 10, 14, 18, 5))


print("----------------------------------------")


#задание 16
def have_trains_crashed(v1, v2):
    total_distance = 10
    first_segment = 4
    second_segment = total_distance - first_segment
    time_train_1 = first_segment / v1
    time_train_2 = second_segment / v2

    if time_train_1 >= time_train_2:
        return True
    else:
        return False

#print(have_trains_crashed(20, 30))

if have_trains_crashed(40, 100):
    print("Trains will crash!")
else:
    print("Trains won't crash!")

print("----------------------------------------")

#задание 17
print("Решение квадратного уравнения (ax ** 2 + bx + c = 0): ")

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x, None
    else:
        return None, None

result1, result2 = solve_quadratic_equation(4, 256, 8)

if result1 == None and result2 == None:
    print("There are no roots")
elif result2 == None:
    print("x = {:.2f}".format(result1))
else:
    print("Roots are : x1 = {:.2f}, x2 = {:.2f}".format(result1, result2))


print("----------------------------------------")


#задание 18
def sum_symbol_codes(first, last):
    unicode1 = ord(first)
    unicode2 = ord(last)
    total_sum = 0
    for i in range(unicode1, unicode2 + 1):
        total_sum += i
        print(i, total_sum)
    return total_sum

result = sum_symbol_codes("x", "z")
print(result)


print("----------------------------------------")

#задание 19
def diff_min_max(num_limit, lower_bound, upper_bound):
    current_min = upper_bound
    current_max = lower_bound
    for i in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)

        if current_min > rand_num:
            current_min = rand_num
        elif current_max < rand_num:
            current_max = rand_num

    return current_max - current_min

print("###################")
print("Difference of max and min:", diff_min_max(5, 100, 200))

print("----------------------------------------")

#задание 20
def diff_even_odd(num_limit, lower_bound, upper_bound):
    total_even = 0
    total_odd = 0
    for i in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)

        if rand_num % 2 == 0:
            total_even = total_even + rand_num
        elif rand_num % 2 != 0:
            total_odd = total_odd + rand_num

    return total_even - total_odd

print("###################")
print("Difference of even and odd:", diff_even_odd(10, 50, 100))

print("----------------------------------------")
















