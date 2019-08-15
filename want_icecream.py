want_input = input("You want a icecream? (Yes / No): ").upper()

if want_input == "YES":
    want = True
elif want_input == "NO":
    want = False
else:
    want = False
    print("I don´t understand that, I guess not")

money_input = input("You have enough money? (Yes / No): ").upper()

if money_input == "YES":
    money = True
elif money_input == "NO":
    money = False
else:
    money = False
    print("I don´t understand that, I guess not")

icecream_guy_input = input("Is out there the icecream´s guy? (Yes / No): ").upper()

if icecream_guy_input == "YES":
    icecream_guy = True
elif icecream_guy_input == "NO":
    icecream_guy = False
else:
    icecream_guy = False
    print("I don´t understand that, I guess not")

uncle_input = input("Is there your uncle to give you some money? (Yes / No): ").upper()

if uncle_input == "YES":
    uncle = True
elif uncle_input == "NO":
    uncle = False
else:
    uncle = False
    print("I don´t understand that, I guess not")

if want and money or uncle and icecream_guy:
    print("So go and get some icecream")
else:
    print("So sad, then drink water")


    