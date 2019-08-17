user_text = input("Add a quote: ")
dot = "."
comma = ","
space = " "

n_dot = 0
n_comma = 0
n_space = 0

for word in user_text:
    if word == dot:
        n_dot += 1
    elif word == comma:
        n_comma += 1
    elif word == space:
        n_space += 1

print("there is {} dots".format((n_dot)))
print("{} spaces".format((n_space)))
print("and {} comma".format(n_comma))