"""07_delete_card_v1.
The first version of the 'Delete Card' function."""

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

# Asks the user to input an existing card they want to delete
card_delete = input("Type the name of the card you want to delete (use capitals where necessary): ")

# Checks if the card exists
delete_card = None
for card in cards:
    if card['Name'] == card_delete:
        delete_card = card
        break

# Display searched card
if delete_card:
    print(f"\nBelow is the stats of {delete_card['Name']}, the card you are about delete.")
    # Sorts each stat for searched monster downwards without curly brackets or commas
    print(f"\nName: {delete_card['Name']}")
    print(f"Strength: {delete_card['Strength']}")
    print(f"Speed: {delete_card['Speed']}")
    print(f"Stealth: {delete_card['Stealth']}")
    print(f"Cunning: {delete_card['Cunning']}")

    while True:
        # Confirm with user if they want to delete
        confirm_delete = input(f"\nAre you sure want to delete {delete_card['Name']}? (Please enter 'Yes' or 'No'): ")

        # If user inputs 'Yes,' delete the card
        if confirm_delete == "Yes":
            cards.remove(delete_card)
            break

        # If user inputs 'No,' break
        elif confirm_delete == "No":
            break

        # Error message if user inputs anything else
        else:
            print("Please enter a valid input.")

# Error message if user searches for a card or anything not from the list
else:
    print("\nCard not found")

print("\n*** Updated Monster Names and Stats ***")
for monster in cards:
    # Sorts each stat for each monster downwards without curly brackets or commas
    print(f"\nName: {monster['Name']}")
    print(f"Strength: {monster['Strength']}")
    print(f"Speed: {monster['Speed']}")
    print(f"Stealth: {monster['Stealth']}")
    print(f"Cunning: {monster['Cunning']}")
