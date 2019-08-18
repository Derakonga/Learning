user_numbers = []
user_num = ""
while len(user_numbers) < 10:
    while not user_num.isdigit():
        user_num = input("Add a number: ")
    user_numbers.append(int(user_num))
    user_num = ""
    print("Number added!")

low_num = user_numbers[0]

for number in user_numbers:
    if number < low_num:
        low_num = number

print("The lower number is {}".format(low_num))