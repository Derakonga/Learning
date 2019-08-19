string_list = ["Hello", "Sun", "Institution", "Welcome"]
n_word = 0

for string in string_list:
    for word in string:
        n_word += 1
    print("{} have {} words".format(string, n_word))
    n_word = 0

