print("This is a puzzle favored by Einstein. You will be asked to enter a three digit number, where the hundred's digit"
   "differs from the one's digit by at least two. The procedure will always yield 1089")

input_number = input('Give me a number --> ')

if len(input_number) == 3 and abs(int(input_number[0]) - int(input_number[2])) >= 2:
    print("The quantity of digits in your number is right!")
else:
    print("There should be 3 digits in your number!")
    input_number = input('Give me a number --> ')

def reverse(number):
        return int(str(number)[::-1])

print("For the number:", input_number, "the reverse number is:", reverse(input_number))

difference = abs(int(input_number) - int(reverse(input_number)))
print("The difference between {} and {} is {}".format(input_number, reverse(input_number), difference))
print("The reverse difference is", reverse(difference))
sum = difference + reverse(difference)
print("The sum of {} and {} is {}".format(difference, reverse(difference), sum))





