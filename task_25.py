# Задание 25!
# Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию, которая переставляет его элементы
# в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
# Примечание: использовать метод random.shuffle не допускается.
# def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
#     pass

import random
# odd_list = [i for i in range (1, 100, 2)]
odd_list = [i for i in range(1, 100) if i % 2 != 0]
print(len(odd_list))
print(odd_list)

def shuffle_list(list_to_shuffle):
    for i in range(len(list_to_shuffle) - 1):
        index1 = random.randint(0, len(list_to_shuffle) - 1)
        index2 = random.randint(0, len(list_to_shuffle) - 1)
        temp = list_to_shuffle[index1]
        list_to_shuffle[index1] = list_to_shuffle[index2]
        list_to_shuffle[index2] = temp
        # list_to_shuffle[index1], list_to_shuffle[index2] = list_to_shuffle[index2], list_to_shuffle[index1]

    return list_to_shuffle


print(shuffle_list(odd_list))



