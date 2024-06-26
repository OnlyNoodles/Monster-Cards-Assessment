"""06_add_card_v1."""

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


new_card = {}
new_card['Name'] = input("Enter the name of your new monster: ")
new_card['Strength'] = int(input("Enter the new monster's strength number: "))
new_card['Speed'] = int(input("Enter the new monster's speed number: "))
new_card['Stealth'] = int(input("Enter the new monster's stealth number: "))
new_card['Cunning'] = int(input("Enter the new monster's cunning number: "))

cards.append(new_card)
print("\nCard added successfully")
print(f"\nName: {new_card['Name']}")
print(f"Strength: {new_card['Strength']}")
print(f"Speed: {new_card['Speed']}")
print(f"Stealth: {new_card['Stealth']}")
print(f"Cunning: {new_card['Cunning']}")
