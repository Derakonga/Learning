a = 0
while a < 5:
    number_to_guess = 3
    user_number = int(input("Guess a number: "))
    if user_number == number_to_guess:
        print("You WIN")
        a = 5
    else:
        print("You LOSE, try again")
        a = a + 1
