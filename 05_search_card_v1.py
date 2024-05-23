"""05_search_cards_v1.
Program will ask the user for the card they want to search up from the list
and the program will output the name and the stats of the monster.
If the card is not found, an error message will pop up."""

# List of cards
cards = [{"Name": "Stoneling", "Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
         {"Name": "Vexscream", "Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
         {"Name": "Dawnmirage", "Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
         {"Name": "Blazegolem", "Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
         {"Name": "Websnake", "Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
         {"Name": "Moldvine", "Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
         {"Name": "Vortexwing", "Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
         {"Name": "Rotthing", "Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
         {"Name": "Froststep", "Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
         {"Name": "Whispghoul", "Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}]

# Ask the user for what combo they want to search
card_search = input("Type the name of the card you want to search for (use capitals where necessary): ")

# Checks if card exists
found_card = None
for card in cards:
    if card['Name'] == card_search:
        found_card = card
        break

# Display result
if found_card:
    # Sorts each stat for searched monster downwards without curly brackets or commas
    print(f"\nName: {found_card['Name']}")
    print(f"Strength: {found_card['Strength']}")
    print(f"Speed: {found_card['Speed']}")
    print(f"Stealth: {found_card['Stealth']}")
    print(f"Cunning: {found_card['Cunning']}")

else:
    print("\nCard not found")
