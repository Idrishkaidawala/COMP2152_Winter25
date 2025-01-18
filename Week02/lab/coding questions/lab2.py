import random

# Defining the weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

try:
    # Roll the dice (1-6)
    weaponRoll = random.randint(1, 6)

    # Print the weaponRoll and corresponding weapon
    print(f"Weapon roll: {weaponRoll}")
    hero_weapon = weapons[weaponRoll - 1]
    print(f"Hero's weapon: {hero_weapon}")

    # Define the conditions
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    if hero_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

    # Add error handling for inputs (example: combat strength input)
    while True:
        combat_strength = input("Enter hero's combat strength: ")
        if combat_strength.isdigit():
            combat_strength = int(combat_strength)
            break
        else:
            print("Error: Combat strength must be an integer. Please try again.")

    combat_strength += weaponRoll
    print(f"Hero's updated combat strength: {combat_strength}")

except ValueError as e:
    print(f"Error: {e}")
