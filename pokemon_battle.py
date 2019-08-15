enemy_dmg = 0
enemy_life = 0
pika_life = 100
chosen_pokemon = input("Against which Pokemon do you want to fight? (Squirtle / Charmander / Bulbasaur): ")

if chosen_pokemon == "Squirtle":
    enemy_dmg = 8
    enemy_life = 90
elif chosen_pokemon == "Charmander":
    enemy_dmg = 7
    enemy_life = 80
elif chosen_pokemon == "Bulbasaur":
    enemy_dmg = 10
    enemy_life = 100

while pika_life > 0 and enemy_life > 0:

    chosen_move = input("What attack do you want to use? (Quick attack / Thunderbolt): ")
    if chosen_move == "Quick attack":
        enemy_life -= 10
    elif chosen_move == "Thunderbolt":
        enemy_life -= 12

    print("The life of the {} is now {}".format(chosen_pokemon, enemy_life))
    print("{} hits you with an {} damage attack".format(chosen_pokemon, enemy_dmg))
    pika_life  -= enemy_dmg
    print("Pikachu has {} life left".format(pika_life))

if enemy_life <= 0:
    print("{} has been defeated, YOU WIN!".format(chosen_pokemon))
elif pika_life <= 0:
    print("Pikachu can´t continue, YOU LOSE!")

print("The battle is over!")