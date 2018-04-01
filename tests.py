#task 1
a = 15
b = 5
c = 2

result = (a + b * c) ** 2
print("Результат (a + b * c) ** 2 при a = {}, b = {}, c = {} равен: {:.2f}".format(a, b, c, result))

#task 2
result1 = a - 4 * b / c
formula = "(a - 4 * b / c)"
print("Результат %s при a = %d, b = %d, c = %d равен: %.2f" % (formula, a, b, c, result1))

#task 3
result2 = (a * b + 4) / (c - 1)
print("Результат (a * b + 4) / (c - 1) при a = {}, b = {}, c = {} равен: {:.2f}".format(a, b, c, result2))

#task 4
#Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры
input_number = input("Введите 5-значное число:")
multiply_of_odd_digits_in_number = 1
for i in input_number:
    if int(i) % 2 != 0 and int(i) != 0:
        multiply_of_odd_digits_in_number *= int(i)
        #multiply_of_odd_digits_in_number = multiply_of_odd_digits_in_number * i

print("Произведение нечетных цифр 5-значного числа = {}".format(multiply_of_odd_digits_in_number))

#task 5
# Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
# Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.
comparable_number1 = 8.5
comparable_number2 = 11.45
number = 10
difference1 = abs(number - comparable_number1)
difference2 = abs(number - comparable_number2)
if difference1 == difference2:
    print("The first {} and the second {} comparable numbers have an equal distance from number {}!"
          .format(comparable_number1, comparable_number2, number))
elif difference1 > difference2:
    print("The second comparable number {} is closer to number {},"
          "than the first comparable number {}!".format(comparable_number2, number, comparable_number1))
elif difference1 < difference2:
    print("The first comparable number {} is closer to number {},"
          "than the second comparable number {}!".format(comparable_number1, number, comparable_number2))


