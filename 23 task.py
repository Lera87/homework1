# Задание 23!
# Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную,
# на первый взгляд, награду: столько пшеничных зёрен, сколько окажется на шахматной доске, если на первую клетку положить
# одно зерно, на вторую — два зерна, на третью — четыре зерна и т. д.
# Оказалось, что такого количества зерна нет на всей планете (оно равно 2**64 − 1 зерен).
# Посчитайте, начиная с какой клетки по счету, общее количество зерен, которое должен был бы отдать раджа изобретателю
# было больше 1 000 000 зерен и сколько конкретно зерен он должен был бы отдать.
# def chess_reward(): # returns 2 ints (cell number and total number of corns)

def chess_reward():
    current_cell_number = 1
    current_cell_corns = 1
    total_corns = 1
    while total_corns < 1000000:
        current_cell_corns *= 2
        current_cell_number += 1
        total_corns += current_cell_corns

    return current_cell_number, total_corns

res1, res2 = chess_reward()

print("Total number of corns: {}, while cell number - {}".format(res2, res1))








