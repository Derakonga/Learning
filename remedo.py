user_input = input("Tell him something!: ")
for word in ["A", "a", "e", "E", "o", "O", "u", "U"]:
    if word in user_input:
         user_input = user_input.replace(word, "i")
print(user_input)
