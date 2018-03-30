import math
import random

# задание 14
# Написать функцию, которая будет проверять четность некоторого числа.
# def is_even(number): # returns boolean value
#     pass

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


# задание 15
# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости. Каждая окружность задается координатами центра и радиусом.
# def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
#     pass

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


# задание 16
# Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.
# def have_trains_crashed(v1, v2): # returns boolean value
#     pass

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

# задание 17
# Написать функцию решения квадратного уравнения.
# def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots, 1 root and None or 2 Nones
#     pass

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


# задание 18
# Каждому символу в таблице символов Unicode соответствует число. Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам, стоящим между двумя заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.
# def sum_symbol_codes(first, last): # returns int
#     pass

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

# задание 19
# Написать функцию для поиска разницы между максимальным и минимальным числом среди num_limit случайно сгенерированных чисел в указанном числовом диапазоне.
# def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
#     pass

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

# задание 20
# Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди num_limit случайно сгенерированных чисел в указанном числовом диапазоне. Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
# def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
#     pass


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
print("Difference between even and odd:", diff_even_odd(10, 50, 100))

print("----------------------------------------")

# задание 21
# Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
# def get_max_digit(number): # returns int
#     pass

rand_num = random.randint(100000000000, 999999999999)
print("Случайно сгенерированное 12-значное число:", rand_num)

def get_max_digit(rand_num):
    rand_num_str = str(rand_num)
    max_number = "0"
    for digit in rand_num_str:
        if digit > max_number:
            max_number = digit

    return max_number

print("Max number is :",get_max_digit(rand_num))

print("----------------------------------------")























