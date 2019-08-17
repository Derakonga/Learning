my_list = []
user_input = input("What you want to buy?: ")

while user_input != "END":
    my_list.append(user_input)
    user_input = input("What you want to buy?: ")
for item in my_list:
    print("You have to buy {}".format(item))
print("that´s all you need")
