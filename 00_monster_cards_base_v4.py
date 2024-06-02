"""00_monster_cards_base_v4.
Added the 'Search Cards' function (05_search_cards_v6)
to 00_monster_cards_v3 and to the option's menu to test it
against the rest of the program."""


import easygui

# List of Cards
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
    answer = easygui.buttonbox(msg=question_text, choices=["Yes", "No"], title="Been Here Before?")

    # If they say yes or no, return their answer
    return answer


# Function to display instructions
def instructions():
    # Instructions
    easygui.msgbox(msg="To output the all cards to the Python console, select 'Output Cards.'\n"
                       "To search for a card, select 'Search and Edit Cards.'"
                       "Selecting this will also give you a choice to edit the card"
                       "you have searched for, such as its name and stats.\n"
                       "To add a card, select 'Add Card.'\n"
                       "To delete a card, select 'Delete Card.'\n"
                       "To exit 'Monster Cards,' select 'Exit.'", title="Instructions")


# Function for outputting cards
def output_cards():
    # Outputs the list of cards
    print("\n*** Monster names and stats ***")
    for monster in cards:
        # Sorts each stat for each monster downwards without curly brackets or commas
        print(f"\nName: {monster['Name']}")
        print(f"Strength: {monster['Strength']}")
        print(f"Speed: {monster['Speed']}")
        print(f"Stealth: {monster['Stealth']}")
        print(f"Cunning: {monster['Cunning']}")


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

                # If user selects 'Yes,' proceed to edit menu
                if edit_choice == "Yes":
                    stat_to_edit = easygui.buttonbox(msg="Which stat do you want to edit?",
                                                     choices=['Name', 'Strength', 'Speed',
                                                              'Stealth', 'Cunning', 'Cancel'],
                                                     title="Edit Menu")

                    # If user selects 'Cancel,' go back to search
                    if stat_to_edit == 'Cancel':
                        break

                    # If user selects 'Name,' proceed to 'edit name' question
                    elif stat_to_edit == 'Name':
                        while True:
                            new_name = easygui.enterbox(msg=f"Enter the new name for {found_card['Name']}.\n"
                                                        f"To go back, select 'Cancel.'",
                                                        title=f"Edit {found_card['Name']}'s Name")

                            # If user selects 'Cancel,' go back to 'edit card' question
                            if new_name is None or new_name == "Cancel":
                                break

                            # Check if the entered name is already taken
                            if new_name and new_name not in [card['Name'] for card in cards]:
                                found_card['Name'] = new_name
                                easygui.msgbox(msg=f"Name has been updated to {new_name}.",
                                               title="Name Edited")
                                break
                            else:
                                easygui.msgbox(msg=f"The name {new_name} is already taken or invalid. "
                                                   f"Please enter a unique name.", title="Error")

                        if new_name is None or new_name == "Cancel":
                            continue

                    # If user selects to edit a stat, proceed to 'stat edit' question
                    elif stat_to_edit in ['Strength', 'Speed', 'Stealth', 'Cunning']:
                        new_value = easygui.integerbox(msg=f"Enter the new whole number integer for {stat_to_edit} "
                                                       f"(1-25).\n To go back, select 'Cancel.'"
                                                       , upperbound=25, lowerbound=1,
                                                        title=f"Edit {found_card['Name']}'s {stat_to_edit}")

                        # If user selects 'Cancel,' go back to 'edit card' question
                        if new_value is None or new_value == "Cancel":
                            continue

                        # Update card stat
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

        # If user inputs card not in list, show error message
        else:
            easygui.msgbox(msg="\nCard not found", title="Error")


# Main routine

# Welcome Message
easygui.msgbox("***Welcome to Monster Cards!***")
# Asks for name
name = easygui.enterbox("Please enter your name: ")
# Combines welcome message and name
easygui.msgbox(f"Welcome to the Monster Cards, {name}!")
# Question on whether the user has used the program before
played_before = yes_no("Have you used 'Monster Cards' before?\n"
                       "(Select 'Yes' to go to the option's menu.\n "
                       "Select 'No' to view the instructions.)")

# If user selects 'No,' output instructions
if played_before == "No":
    instructions()

# Loop for option's menu so that it keeps re-asking the question after every function until the user exits
while True:
    # Ask the user what they want to do
    option = easygui.buttonbox(msg="What would you like to do?", title="Option's Menu",
                               choices=["Display Instructions", "Output Cards", "Search and Edit Cards", "Exit"])

    # If user selects 'Display Instructions,' run instructions() function
    if option == "Display Instructions":
        instructions()

    # If user selects 'Output Cards,' run output_cards() function
    elif option == "Output Cards":
        output_cards()

    # If user selects 'Search and Edit Cards,' run search_and_edit() function
    elif option == "Search and Edit Cards":
        search_and_edit()

    # If user selects 'Exit,' exit the program
    elif option == "Exit":
        break
