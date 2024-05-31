"""06_add_card_v3.
Implemented a while loop so that
the program will re-ask the user
if they select 'Cancel' for the
name or input nothing."""

import easygui

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


while True:
    new_card = {}
    new_card['Name'] = easygui.enterbox("Enter the name of your new monster.\n"
                                        "To go back to the option's menu, select 'Cancel.'")

    if new_card['Name'] is None or new_card['Name'] == "Cancel":
        break
    new_card['Strength'] = easygui.integerbox("Enter the new monster's strength number (whole number of 1-25)",
                                              upperbound=25, lowerbound=1)
    new_card['Speed'] = easygui.integerbox("Enter the new monster's speed number (whole number of 1-25)",
                                              upperbound=25, lowerbound=1)
    new_card['Stealth'] = easygui.integerbox("Enter the new monster's stealth number (whole number of 1-25)",
                                              upperbound=25, lowerbound=1)
    new_card['Cunning'] = easygui.integerbox("Enter the new monster's cunning number (whole number of 11-25)",
                                              upperbound=25, lowerbound=1)

    cards.append(new_card)
    easygui.msgbox(msg=f"\nName: {new_card['Name']}\n"
                                   f"Strength: {new_card['Strength']}\n"
                                   f"Speed: {new_card['Speed']}\n"
                                   f"Stealth: {new_card['Stealth']}\n"
                                   f"Cunning: {new_card['Cunning']}",
                               title="Card added successfully")
