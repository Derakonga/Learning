user_input = input("Add a quote: ")
n_caps = 0

for word in user_input:
    if (word.isupper()):
        n_caps += 1




print("There is {} caps".format(n_caps))