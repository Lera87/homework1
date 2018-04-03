# Задание 25
# Для удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы в зависимости от
# первых букв их фамилии. Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’. Название группы определяет в какую группу
# попадает абитуриент, в зависимости от первой буквы его/ее фамилии. Например, Will Smith попадает в
# группу ‘Q-T’, т.к. первая буква его фамилии попадает в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).
# Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д. Написать функцию, которая получает список имен студентов
# вида ['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...] и возвращает количество абитуриентов в группах,
# сформированных по их фамилиям, описанным выше образом.
# def group_by_surname(list_of_enrollees): # returns 4 ints
#     pass

def group_by_surname(list_of_enrollees):
    group_of_students1 = 0
    group_of_students2 = 0
    group_of_students3 = 0
    group_of_students4 = 0
    for i in range(len(list_of_enrollees)):
        names_separately = list_of_enrollees[i].split(' ')
        print(names_separately)
        surname = names_separately[1]
        first_surname_letter = surname[0]
        if 'A' <= first_surname_letter <= 'I':
            group_of_students1 += 1
        elif 'J' <= first_surname_letter <= 'P':
            group_of_students2 += 1
        elif 'Q' <= first_surname_letter <= 'T':
            group_of_students3 += 1
        elif 'U' <= first_surname_letter <= 'Z':
            group_of_students4 += 1

    return group_of_students1, group_of_students2, group_of_students3, group_of_students4


list_of_enrollees = ['Megan Fox', 'John Williams', 'Peter Jameson', 'Meredith White', 'Ann Scott', 'Elizabeth Barns']
print(group_by_surname(list_of_enrollees))

