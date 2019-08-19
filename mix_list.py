list = ["Hello", 23, "Sun", 10, "College", 5, "Goodbye", 100]
string_list = []
number_list = []
for each in list:
    if type(each) == int:
        number_list.append(each)

    elif type(each) == str:
        string_list.append(each)

print(string_list)
print(number_list)




