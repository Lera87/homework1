print("We are going to play a game. I want you to pick a number then do a series of calculations. "
      "I bet I know the resultof those calculations will be!")

input_your_choice = input("*You* This will be the answer. Select a number 10-49 --> ")
input_player_choice = input("*Player* Pick any number 50-99 --> ")

factor = 99 - int(input_your_choice)
print("The factor is", factor)
sum_factor_player_choice = factor + int(input_player_choice)
print("The sum of factor and players' choice is", sum_factor_player_choice)
hundreds_digit = int(sum_factor_player_choice) % 100
# unit_digit = int(sum_factor_player_choice) // 100
unit_digit = str(sum_factor_player_choice)[0]
sum_hundreds_unit_digit = hundreds_digit + int(unit_digit)
print("The sum of hundred's digit and unit digit is", sum_hundreds_unit_digit)
answer = (abs(int(input_player_choice) - sum_hundreds_unit_digit))
# print(answer)
print("I said the answer was {} and the calculation result is {}!".format(input_your_choice, answer))
