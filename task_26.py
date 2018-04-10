# Создайте список из 11 случайных целых чисел из отрезка [-1;1]. Передайте его в функцию, которая определит
# какой элемент встречается в списке чаще всего и вернет этот элемент. Однако, если два каких-то элемента
# встречаются одинаковое количество раз, то вернуть None, а не самый часто встречающийся элемент, даже
# если дублирующиеся элементы не максимальны!
# def calc_frequency(lst): # returns the most frequent number or None
#     pass

import random

lst = [random.randint(-1, 1) for i in range(11)]
print(lst)
def calc_frequency(lst):
    frequency_of_symbols = {}
    for i in lst:
        frequency_of_symbols[i] = frequency_of_symbols.get(i, 0) + 1
    print(frequency_of_symbols)
    if frequency_of_symbols[0] == frequency_of_symbols[1] or \
                    frequency_of_symbols[0] == frequency_of_symbols[-1] or \
                    frequency_of_symbols[1] == frequency_of_symbols [-1]:
        return None
    else:
        max_number = 0
        max_key = 0
        for key in frequency_of_symbols:
            if frequency_of_symbols[key] > max_number:
                max_number = frequency_of_symbols[key]
                max_key = key
        return max_key

print(calc_frequency(lst))



