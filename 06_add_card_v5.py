"""06_add_card_v5.
Turned 06_add_card_v4 into a function.
Added titles to all easygui boxes.
Made it so that when the user click 'Cancel'
when choosing a name, the code breaks safely
with no error message, which would mean going
back to the option's menu when tested in the
base code.
This is the version I will use in
00_monster_cards_base_v5 and the future
versions of 00_monster_cards_base."""

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


# Function for adding a new card
def add_card():
    while True:
        new_card = {}

        while True:
            # Ask user to input monster name
            new_card['Name'] = easygui.enterbox(msg="Enter the name of your new monster.\n"
                                                "To go back to the option's menu, select 'Cancel.'",
                                                title="Add New Card's Name")

            # Exit the function if 'Cancel' is selected
            if new_card['Name'] is None:
                return

            # Check if the entered name is already taken
            if new_card['Name']:
                if any(monster['Name'] == new_card['Name'] for monster in cards):
                    easygui.msgbox(msg=f"The name {new_card['Name']} is already taken", title="Error")
                else:
                    break

            # Re-ask the question if user inputs nothing
            elif new_card['Name'].strip() == "":
                easygui.msgbox(msg="Please enter a name for your monster.", title="Error")

        # Ask the user for 'Strength' input
        new_card['Strength'] = easygui.integerbox(msg=f"Enter a whole number of 1-25 for "
                                                  f"{new_card['Name']}'s strength number.\n"
                                                  f"To scrap {new_card['Name']} and go back to the option's menu, "
                                                  f"select 'Cancel.'",
                                                  upperbound=25, lowerbound=1, title=f"Add {new_card['Name']}'s "
                                                                                     f"Strength")

        # Exit the function if 'Cancel' is selected
        if new_card['Strength'] is None:
            break

        # Ask the user for 'Speed' input
        new_card['Speed'] = easygui.integerbox(msg=f"Enter a whole number of 1-25 for "
                                               f"{new_card['Name']}'s speed number.\n"
                                               f"To scrap {new_card['Name']} and go back to the option's menu, "
                                               f"select 'Cancel.'",
                                               upperbound=25, lowerbound=1, title=f"Add {new_card['Name']}'s "
                                                                                     f"Speed")

        # Exit the function if 'Cancel' is selected
        if new_card['Speed'] is None:
            break

        # Ask the user for 'Stealth' input
        new_card['Stealth'] = easygui.integerbox(msg=f"Enter a whole number of 1-25 for "
                                                 f"{new_card['Name']}'s stealth number.\n"
                                                 f"To scrap {new_card['Name']} and go back to the option's menu, "
                                                 f"select 'Cancel.'",
                                                 upperbound=25, lowerbound=1, title=f"Add {new_card['Name']}'s "
                                                                                     f"Stealth")

        # Exit the function if 'Cancel' is selected
        if new_card['Stealth'] is None:
            break

        # Ask the user for 'Cunning' input
        new_card['Cunning'] = easygui.integerbox(msg=f"Enter a whole number integer of 1-25 for "
                                                 f"{new_card['Name']}'s cunning number.\n"
                                                 f"To scrap {new_card['Name']} and go back to the option's menu, "
                                                 f"select 'Cancel.'",
                                                 upperbound=25, lowerbound=1, title=f"Add {new_card['Name']}'s "
                                                                                     f"Cunning")

        # Exit the function if 'Cancel' is selected
        if new_card['Cunning'] is None:
            break

        # Adds cards to the existing list
        cards.append(new_card)

        # Outputs the new card's name and stats
        easygui.msgbox(msg=f"\nName: {new_card['Name']}\n"
                           f"Strength: {new_card['Strength']}\n"
                           f"Speed: {new_card['Speed']}\n"
                           f"Stealth: {new_card['Stealth']}\n"
                           f"Cunning: {new_card['Cunning']}",
                       title="Card added successfully")


add_card()
