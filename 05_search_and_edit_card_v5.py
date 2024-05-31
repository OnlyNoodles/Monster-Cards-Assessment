"""05_search_card_v5.
Changed the program based on user feedback from Alexander Lau.
I changed the code to only accept whole numbers as decimals
is too confusing and makes the stats look overly complicated.
I have also put the whole function into a while loop so that
if the user inputs an invalid card, the program will ask again."""

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
        card_search = easygui.enterbox("Type the name of the card you want to search for "
                                       "(use capitals where necessary).\n "
                                       "To go back to the option's menu, select 'Cancel.'")

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
                edit_choice = easygui.buttonbox(msg=f"Do you want to edit {found_card['Name']}?", choices=["Yes", "No"])
                if edit_choice == "Yes":
                    stat_to_edit = easygui.buttonbox(msg="Which stat do you want to edit?",
                                                     choices=['Name', 'Strength', 'Speed', 'Stealth', 'Cunning'])

                    if stat_to_edit == 'Name':
                        new_name = easygui.enterbox(f"Enter the new name for the monster")
                        found_card['Name'] = new_name
                        easygui.msgbox(f"Name has been updated to {new_name}.")

                    elif stat_to_edit in ['Strength', 'Speed', 'Stealth', 'Cunning']:
                        new_value = easygui.integerbox(f"Enter the new whole number value for {stat_to_edit} (1-25): ",
                                                       upperbound=25, lowerbound=1)
                        found_card[stat_to_edit] = new_value
                        easygui.msgbox(f"{stat_to_edit} has been updated to {new_value}.")

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
            easygui.msgbox("\nCard not found")


search_and_edit()
