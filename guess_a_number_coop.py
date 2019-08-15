number_to_guess = int(input("Choose a number to guess, hide  it from your partner: "))

a = 0
while a < 1:
    user_number = int(input("Now guess the number: "))
    if user_number == number_to_guess:
        print("You WIN")
        a = 1
    else:
        print("You LOSE")

