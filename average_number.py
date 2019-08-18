user_numbers = []
user_num = ""
n_num = 0
finish = ""

while finish != "Yes":
    while not user_num.isdigit():
            user_num = input("Add a number: ")
    user_numbers.append(int(user_num))
    user_num = ""
    print("Number added!")
    n_num += 1
    finish = input("END? (Yes / No): ")

addnum = sum(user_numbers)
average_num = addnum / n_num
print("the average number is {}".format(average_num))

