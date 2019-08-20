string = "aurora boreal"
number = 0

for word in string:
    if word == "a":
        number += 1
        string = string.replace(word, "{}".format(number), 1)
    elif word == "e":
        number += 1
        string = string.replace(word, "{}".format(number), 1)
    elif word == "i":
        number += 1
        string = string.replace(word, "{}".format(number), 1)
    elif word == "o":
        number += 1
        string = string.replace(word, "{}".format(number), 1)
    elif word == "u":
        number += 1
        string = string.replace(word, "{}".format(number), 1)

print(string)