"""03_storing_cards_v2.
Storing all the automatically available cards
in a dictionary but storing the attributes as lists.
This will be trialled against 03_storing_cards_v1."""

# Dictionary of Cards
cards = {"Stoneling": [7, 1, 25, 15], "Vexscream": [1, 6, 21, 19], "Dawnmirage": [5, 15, 18, 22],
         "Blazegolem": [15, 20, 23, 6], "Websnake": [7, 15, 10, 5], "Moldvine": [21, 18, 14, 5],
         "Vortexwing": [19, 13, 19, 2], "Rotthing": [16, 7, 4, 12], "Froststep": [14, 14, 17, 4],
         "Whispghoul": [17, 19, 3, 2]}


# Trialling 1
for name, stats in cards.items():
    print(f"\nName: {name}")
    print(f"Strength: {stats[0]}")
    print(f"Speed: {stats[1]}")
    print(f"Stealth: {stats[2]}")
    print(f"Cunning: {stats[3]}")
