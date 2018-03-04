import math

a = 20
b = 50
c = 16

print("1 задание")
result1 = a + b * (c / 2)
print("Результат при a %d, b %d, c %d равен: (a + b * (c / 2) = %.2f" % (a, b, c, result1))
#print("Результат при a {}, b {}, c {} равен: (a + b * (c / 2) = {:.2f}".format(a, b, c, result1))

print("2 задание")
#result2 = (a**2 + b**2) % 2
result2 = math.fmod(a**2 + b**2, 2)
formula = "(a**2 + b**2) % 2"
#print("Результат при a {}, b {}, c {} равен: (a**2 + b**2) % 2= {:.2f}".format(a, b, c, result2))
print("Результат при a %d, b %d, c %d равен: %s = %.2f" % (a, b, c, formula, result2))

print("3 задание")
x = (a + b) / 12 * c
result3 = math.fmod(x, 4) + b
#второй вариант ввода result3 без ввода новых переменных
#result3 = math.fmod((a + b) / 12 * c, 4) + b
formula = "(a + b) / 12 * c % 4 + b"
print("Результат при a %d, b %d, c %d равен: %s = %.2f" % (a, b, c, formula, result3))
#print("Результат при a {}, b {}, c {} равен: (a + b) / 12 * c % 4 + b = {:.2f}".format(a, b, c, result3))

print("4 задание")
x = (a - b * c) / (a + b)
result4 = math.fmod(x, c)
#второй вариант ввода result4 без ввода новых переменных
#result4 = math.fmod((a - b * c) / (a + b), c)
formula = "(a - b * c) / (a + b) % c"
print("Результат при a %d, b %d, c %d равен: %s = %.2f" % (a, b, c, formula, result4))
#print("Результат при a {}, b {}, c {} равен: (a - b * c) / (a + b) % c = {:.2f}".format(a, b, c, result4))

print("5 задание")
formula = "|a - b| / (a + b)**3 - cos(c)"
#result5 = abs(a - b) / (a + b)**3 - math.cos(c)
result5 = math.fabs(a-b) / (a + b)**3 - math.cos(c)
print("Результат при a %d, b %d, c %d равен: %s = %.2f" % (a, b, c, formula, result5))
#print("Результат при a {}, b {}, c {} равен: |a - b| / (a + b)**3 - cos(c) = {:.2f}".format(a, b, c, result5))

print("6 задание")
formula = "(ln(1 + c) / -b)**4 + |a|"
result6 = (math.log((1+c)) / -b)**4 + abs(a)
#result6 = (math.log((1+c)) / -b)**4 + math.fabs(a)
print("Результат при a %d, b %d, c %d равен: %s = %.2f" % (a, b, c, formula, result6))
#print("Результат при a {}, b {}, c {} равен: (ln(1 + c) / -b)**4 + |a| = {:.2f}".format(a, b, c, result6))