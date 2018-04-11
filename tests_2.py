import random

# Задание 7
# Найти сумму десяти первых чисел ряда Фибоначчи.

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def fibonacci_sum(n):
    fibonacci_list = [fib(i) for i in range(1, n+1)]
    sum_fibonacci = sum(fibonacci_list)
    print('Список первых 10 чисел Фибоначчи', fibonacci_list)
    print('Сумма 10 чисел Фибоначчи = ', sum_fibonacci)


fibonacci_sum(10)


# Задание 9
# Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к интервалу
# [-1;1], причем максимальное абсолютное значение элементов после нормирование должно быть равно 1.
# Например, последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]

list = [random.randint(-1, 10) for i in range(8)]
print("Одномерный список случайных чисел:", list)
def ration_list(list):
    max_number = max([abs(number) for number in list])
    rationed_list = [(digit/max_number) for digit in list]
    return rationed_list


print("Нормированный список", ration_list(list))