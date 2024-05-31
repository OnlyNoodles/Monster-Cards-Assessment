"""05_search_card_v6.
Based on user feedback from Eleasha Chan,
I changed the program so that the user can cancel their choice
if they don't want to edit the card but said they wanted to edit
by mistake. Also made it so that the user has to type something into
easygui.enterbox() when changing the name of an existing monster.
Added titles to all easygui boxes.
This is the version I will use in 00_monster_cards_base_v4 and the future
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


# Function for searching for and editing card
def search_and_edit():
    while True:
        # Ask the user for what combo they want to search
        card_search = easygui.enterbox(msg="Type the name of the card you want to search for "
                                       "(use capitals where necessary).\n "
                                       "To go back to the option's menu, select 'Cancel.'",
                                       title="Search for Card")

        # Returns user to option's menu if user selects 'Cancel'
        if card_search is None or card_search == "Cancel":
            return

        # Checks if card exists
        found_card = None
        for card in cards:
            if card['Name'] == card_search:
                found_card = card
                break

        # Display the result
        if found_card:
            # Sorts each stat for searched monster downwards without curly brackets or commas
            easygui.msgbox(msg=f"\nName: {found_card['Name']}\n"
                               f"Strength: {found_card['Strength']}\n"
                               f"Speed: {found_card['Speed']}\n"
                               f"Stealth: {found_card['Stealth']}\n"
                               f"Cunning: {found_card['Cunning']}",
                           title=found_card['Name'])

            while True:
                # Ask the user if they want to edit the card
                edit_choice = easygui.buttonbox(msg=f"Do you want to edit {found_card['Name']}?",
                                                choices=["Yes", "No"], title="Confirm Edit")
                if edit_choice == "Yes":
                    stat_to_edit = easygui.buttonbox(msg="Which stat do you want to edit?",
                                                     choices=['Name', 'Strength', 'Speed',
                                                              'Stealth', 'Cunning', 'Cancel'],
                                                     title="Stats to Edit")

                    if stat_to_edit == 'Cancel':
                        break

                    if stat_to_edit == 'Name':
                        while True:
                            new_name = easygui.enterbox(msg=f"Enter the new name for the monster",
                                                        title=f"Edit {found_card['Name']}'s Name")
                            # Check if the name is empty
                            if new_name:
                                found_card['Name'] = new_name
                                easygui.msgbox(msg=f"Name has been updated to {new_name}.",
                                               title="Name Edited")
                                break

                            elif new_name is None or new_name == "Cancel":
                                break
                                
                            else:
                                easygui.msgbox("Please enter a name for the monster.", title="Error")

                    elif stat_to_edit in ['Strength', 'Speed', 'Stealth', 'Cunning']:
                        new_value = easygui.integerbox(msg=f"Enter the new whole number value for {stat_to_edit} "
                                                       f"(1-25): ", upperbound=25, lowerbound=1,
                                                        title=f"Edit {found_card['Name']}'s {stat_to_edit}")

                        found_card[stat_to_edit] = new_value
                        easygui.msgbox(msg=f"{stat_to_edit} has been updated to {new_value}.",
                                       title=f"{stat_to_edit} Edited")

                    # Display updated card
                    easygui.msgbox(msg=f"\nName: {found_card['Name']}\n"
                                       f"Strength: {found_card['Strength']}\n"
                                       f"Speed: {found_card['Speed']}\n"
                                       f"Stealth: {found_card['Stealth']}\n"
                                       f"Cunning: {found_card['Cunning']}",
                                   title=f"{found_card['Name']} Updated")

                else:
                    break

        else:
            easygui.msgbox(msg="\nCard not found", title="Error")


search_and_edit()
