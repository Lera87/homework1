import random

#Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
# Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
# После чего опять просит угадать. И так пока пользователь не угадает выбранное число.

computer_choice = random.randint(1, 10)
user_choice = input('Choose a number:')
int_user_choice = int(user_choice)

while int_user_choice != computer_choice:
    if int_user_choice > computer_choice:
        print("Computer number is less than your choice!")
    else:
        print("Computer number is more than your choice!")

    user_choice = input('Choose a number:')
    int_user_choice = int(user_choice)

print("Your choice is right!")