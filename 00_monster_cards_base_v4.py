"""00_monster_cards_base_v4.
Added the 'Search Cards' function (05_search_cards_v6)
to 00_monster_cards_v3 and to the option's menu."""


import easygui

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


# Yes/no checker function
def yes_no(question_text):
    # Ask the user if they have played before
    answer = easygui.buttonbox(msg=question_text, choices=["Yes", "No"])

    # If user says 'Yes' or 'No', return their answer
    return answer


# Instructions function
def instructions():
    easygui.msgbox(msg="To output the all cards to the Python console, select 'Output Cards.'\n"
                       "To search for a card, select 'Search and Edit Cards.'"
                       "Selecting this will also give you a choice to edit the card"
                       "you have searched for, such as its name and stats.\n"
                       "To add a card, select 'Add Card.'\n"
                       "To delete a card, select 'Delete Card.'\n"
                       "To exit 'Monster Cards,' select 'Exit.'", title="Instructions")


# Function for outputting cards
def output():
    # Outputs the list of cards
    print("\n*** Monster names and stats ***")
    for monster in cards:
        # Sorts each stat for each monster downwards without curly brackets or commas
        print(f"\nName: {monster['Name']}")
        print(f"Strength: {monster['Strength']}")
        print(f"Speed: {monster['Speed']}")
        print(f"Stealth: {monster['Stealth']}")
        print(f"Cunning: {monster['Cunning']}")


# Function for number checker
def number_checker(question):
    while True:
        try:
            value = easygui.integerbox(question)
            if 1 <= value <= 25:
                return value
            else:
                easygui.msgbox("Please enter a whole number between 1 and 25.")
        except ValueError:
            easygui.msgbox("Please enter a whole number between 1 and 25.")


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
                                                     choices=['Name', 'Strength', 'Speed',
                                                              'Stealth', 'Cunning', 'Cancel'])

                    if stat_to_edit == 'Cancel':
                        break

                    if stat_to_edit == 'Name':
                        while True:
                            new_name = easygui.enterbox(f"Enter the new name for the monster")
                            # Check if the name is empty
                            if new_name:
                                found_card['Name'] = new_name
                                easygui.msgbox(f"Name has been updated to {new_name}.")
                                break

                            elif new_name is None or new_name == "Cancel":
                                break

                            else:
                                easygui.msgbox("Please enter a name for the monster.")

                    elif stat_to_edit in ['Strength', 'Speed', 'Stealth', 'Cunning']:
                        new_value = number_checker(f"Enter the new whole number value for {stat_to_edit} (1-25): ")
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


# Main routine

# Welcome Message
easygui.msgbox("***Welcome to Monster Cards!***")
# Asks for name
name = easygui.enterbox("Please enter your name: ")
# Combines welcome message and name
easygui.msgbox(f"Welcome to the Monster Cards, {name}!")

played_before = yes_no("Have you used 'Monster Cards' before?\n"
                       "(Select 'Yes' to go to the option's menu.\n "
                       "Select 'No' to view the instructions.)")

if played_before == "No":
    instructions()


while True:
    option = easygui.buttonbox(msg="What would you like to do?", title="Option's Menu",
                               choices=["Display Instructions", "Output Cards", "Search and Edit Cards", "Exit"])

    if option == "Display Instructions":
        instructions()

    elif option == "Output Cards":
        output()

    elif option == "Search and Edit Cards":
        search_and_edit()

    elif option == "Exit":
        break
        