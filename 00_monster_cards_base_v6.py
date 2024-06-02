"""00_monster_cards_base_v6.
Added the 'Delete Card' function (07_delete_card_v4)
to 00_monster_cards_v5 and to the option's menu to test it
against the rest if the program. Made sure that the
program follows PEP8 regulations.
This is the final version of 00_monster_cards_base
and will therefore be the final version of my base code
for 'Monster Cards.'"""


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


# Yes/No Checker function
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
                                                       f"(1-25).\n To go back, select 'Cancel.'",
                                                       upperbound=25, lowerbound=1,
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
        new_card['Strength'] = easygui.integerbox(msg=f"Enter a whole number integer kof 1-25 for "
                                                  f"{new_card['Name']}'s strength number.\n"
                                                  f"To scrap {new_card['Name']} and go back to the option's menu, "
                                                  f"select 'Cancel.'",
                                                  upperbound=25, lowerbound=1, title=f"Add {new_card['Name']}'s "
                                                                                     f"Strength")

        # Exit the function if 'Cancel' is selected
        if new_card['Strength'] is None:
            break

        # Ask the user for 'Speed' input
        new_card['Speed'] = easygui.integerbox(msg=f"Enter a whole number integer of 1-25 for "
                                               f"{new_card['Name']}'s speed number.\n"
                                               f"To scrap {new_card['Name']} and go back to the option's menu, "
                                               f"select 'Cancel.'",
                                               upperbound=25, lowerbound=1, title=f"Add {new_card['Name']}'s "
                                                                                  f"Speed")

        # Exit the function if 'Cancel' is selected
        if new_card['Speed'] is None:
            break

        # Ask the user for 'Stealth' input
        new_card['Stealth'] = easygui.integerbox(msg=f"Enter a whole number integer of 1-25 for "
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


# Function for deleted a card
def delete_card():
    while True:
        # Asks the user to input an existing card they want to delete
        card_delete_question = easygui.enterbox(msg="Type the name of the card you want to delete "
                                                    "(use capitals where necessary).\n\n"
                                                    "To go back to the option's menu, select 'Cancel.'",
                                                title="Delete Card")

        # # Exit the loop if 'Cancel' is selected
        if card_delete_question is None:
            break

        # Checks if the card exists
        card_to_delete = None
        for card in cards:
            if card['Name'] == card_delete_question:
                card_to_delete = card
                break

        # Display searched card
        if card_to_delete:
            # Sorts each stat for searched monster downwards without curly brackets or commas
            easygui.msgbox(msg=f"\nBelow are the stats of {card_to_delete['Name']}, the card you are about delete.\n"
                           f"\nName: {card_to_delete['Name']}\n"
                           f"Strength: {card_to_delete['Strength']}\n"
                           f"Speed: {card_to_delete['Speed']}\n"
                           f"Stealth: {card_to_delete['Stealth']}\n"
                           f"Cunning: {card_to_delete['Cunning']}", title=f"{card_to_delete['Name']}'s stats")

            while True:
                # Confirm with user if they want to delete
                confirm_delete = easygui.buttonbox(msg=f"\nAre you sure want to delete {card_to_delete['Name']}?",
                                                   choices=["Yes", "No"], title="Confirm Deletion")

                # If user inputs 'Yes,' delete the card
                if confirm_delete == "Yes":
                    cards.remove(card_to_delete)
                    easygui.msgbox(msg=f"{card_to_delete['Name']} has been deleted.",
                                   title=f"{card_to_delete['Name']} Deleted")
                    break

                # If user inputs 'No,' break
                elif confirm_delete == "No":
                    break

        # Error message if user searches for a card or anything not from the list
        else:
            easygui.msgbox(msg="\nCard not found", title="Error")


# Main routine

# Welcome Message
easygui.msgbox("***Welcome to Monster Cards!***")
while True:
    # Asks for name
    name = easygui.enterbox("Please enter your name: ")
    if name is None or name == "":
        easygui.msgbox("Please enter your name.")
    else:
        # Combines welcome message and name
        easygui.msgbox(f"Welcome to the Monster Cards, {name}!")
        break
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
                               choices=["Display Instructions", "Output Cards", "Search and Edit Cards",
                                        "Add Card", "Delete Card", "Exit"])

    # If user selects 'Display Instructions,' run instructions() function
    if option == "Display Instructions":
        instructions()

    # If user selects 'Output Cards,' run output_cards() function
    elif option == "Output Cards":
        output_cards()

    # If user selects 'Search and Edit Cards,' run search_and_edit() function
    elif option == "Search and Edit Cards":
        search_and_edit()

    # If user selects 'Add Card,' run add_card() function
    elif option == "Add Card":
        add_card()

    # If user selects 'Delete Card,' run delete_card() function
    elif option == "Delete Card":
        delete_card()

    # If user selects 'Exit,' exit the program
    elif option == "Exit":
        break
