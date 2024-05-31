"""00_monster_cards_base_v7.
Edited the code's structure to follow the PEP8 regulations.
This is the final version of 00_monster_cards_base
and will therefore be the final version of my base code
for 'Monster Cards.'"""

import easygui

# List of Cards
cards = [
    {"Name": "Stoneling", "Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    {"Name": "Vexscream", "Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    {"Name": "Dawnmirage", "Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    {"Name": "Blazegolem", "Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    {"Name": "Websnake", "Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    {"Name": "Moldvine", "Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    {"Name": "Vortexwing", "Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    {"Name": "Rotthing", "Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    {"Name": "Froststep", "Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    {"Name": "Whispghoul", "Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
]


# Yes/No Checker function
def yes_no(question_text):
    answer = easygui.buttonbox(
        msg=question_text, choices=["Yes", "No"], title="Been Here Before?"
    )
    return answer


# Function to display instructions
def instructions():
    easygui.msgbox(
        msg="To output the all cards to the Python console, select 'Output Cards.'\n"
            "To search for a card, select 'Search and Edit Cards.' Selecting this will "
            "also give you a choice to edit the card you have searched for, such as its "
            "name and stats.\n"
            "To add a card, select 'Add Card.'\n"
            "To delete a card, select 'Delete Card.'\n"
            "To exit 'Monster Cards,' select 'Exit.'",
        title="Instructions"
    )


# Function for outputting cards
def output_cards():
    print("\n*** Monster names and stats ***")
    for monster in cards:
        print(f"\nName: {monster['Name']}")
        print(f"Strength: {monster['Strength']}")
        print(f"Speed: {monster['Speed']}")
        print(f"Stealth: {monster['Stealth']}")
        print(f"Cunning: {monster['Cunning']}")


# Function for searching for and editing card
def search_and_edit():
    while True:
        card_search = easygui.enterbox(
            msg="Type the name of the card you want to search for "
                "(use capitals where necessary).\n"
                "To go back to the option's menu, select 'Cancel.'",
            title="Search for Card"
        )

        if card_search is None or card_search == "Cancel":
            return

        found_card = None
        for card in cards:
            if card['Name'] == card_search:
                found_card = card
                break

        if found_card:
            easygui.msgbox(
                msg=f"\nName: {found_card['Name']}\n"
                    f"Strength: {found_card['Strength']}\n"
                    f"Speed: {found_card['Speed']}\n"
                    f"Stealth: {found_card['Stealth']}\n"
                    f"Cunning: {found_card['Cunning']}",
                title=found_card['Name']
            )

            while True:
                edit_choice = easygui.buttonbox(
                    msg=f"Do you want to edit {found_card['Name']}?",
                    choices=["Yes", "No"], title="Confirm Edit"
                )
                if edit_choice == "Yes":
                    stat_to_edit = easygui.buttonbox(
                        msg="Which stat do you want to edit?",
                        choices=['Name', 'Strength', 'Speed', 'Stealth', 'Cunning', 'Cancel'],
                        title="Stats to Edit"
                    )

                    if stat_to_edit == 'Cancel':
                        break

                    if stat_to_edit == 'Name':
                        while True:
                            new_name = easygui.enterbox(
                                msg="Enter the new name for the monster",
                                title=f"Edit {found_card['Name']}'s Name"
                            )
                            if new_name:
                                found_card['Name'] = new_name
                                easygui.msgbox(
                                    msg=f"Name has been updated to {new_name}.",
                                    title="Name Edited"
                                )
                                break

                            elif new_name is None or new_name == "Cancel":
                                break

                            else:
                                easygui.msgbox(msg="Please enter a name for the monster.", title="Error")

                    elif stat_to_edit in ['Strength', 'Speed', 'Stealth', 'Cunning']:
                        new_value = easygui.integerbox(
                            msg=f"Enter the new whole number value for {stat_to_edit} (1-25): ",
                            upperbound=25, lowerbound=1,
                            title=f"Edit {found_card['Name']}'s {stat_to_edit}"
                        )

                        found_card[stat_to_edit] = new_value
                        easygui.msgbox(
                            msg=f"{stat_to_edit} has been updated to {new_value}.",
                            title=f"{stat_to_edit} Edited"
                        )

                    easygui.msgbox(
                        msg=f"\nName: {found_card['Name']}\n"
                            f"Strength: {found_card['Strength']}\n"
                            f"Speed: {found_card['Speed']}\n"
                            f"Stealth: {found_card['Stealth']}\n"
                            f"Cunning: {found_card['Cunning']}",
                        title=f"{found_card['Name']} Updated"
                    )
                else:
                    break
        else:
            easygui.msgbox(msg="\nCard not found", title="Error")


# Function for adding a new card
def add_card():
    while True:
        new_card = {}

        while True:
            new_card['Name'] = easygui.enterbox(
                msg="Enter the name of your new monster.\n"
                    "To go back to the option's menu, select 'Cancel.'",
                title="Add New Card's Name"
            )

            if new_card['Name'] is None:
                return

            elif new_card['Name'].strip() == "":
                easygui.msgbox(msg="Please enter a name for your monster.", title="Error")
            else:
                break

        new_card['Strength'] = easygui.integerbox(
            msg=f"Enter a whole number of 1-25 for {new_card['Name']}'s strength number.\n"
                f"To scrap {new_card['Name']} and go back to the option's menu, select 'Cancel.'",
            upperbound=25, lowerbound=1,
            title=f"Add {new_card['Name']}'s Strength"
        )

        if new_card['Strength'] is None:
            return

        new_card['Speed'] = easygui.integerbox(
            msg=f"Enter a whole number of 1-25 for {new_card['Name']}'s speed number.\n"
                f"To scrap {new_card['Name']} and go back to the option's menu, select 'Cancel.'",
            upperbound=25, lowerbound=1,
            title=f"Add {new_card['Name']}'s Speed"
        )

        if new_card['Speed'] is None:
            return

        new_card['Stealth'] = easygui.integerbox(
            msg=f"Enter a whole number of 1-25 for {new_card['Name']}'s stealth number.\n"
                f"To scrap {new_card['Name']} and go back to the option's menu, select 'Cancel.'",
            upperbound=25, lowerbound=1,
            title=f"Add {new_card['Name']}'s Stealth"
        )

        if new_card['Stealth'] is None:
            return

        new_card['Cunning'] = easygui.integerbox(
            msg=f"Enter a whole number of 1-25 for {new_card['Name']}'s cunning number.\n"
                f"To scrap {new_card['Name']} and go back to the option's menu, select 'Cancel.'",
            upperbound=25, lowerbound=1,
            title=f"Add {new_card['Name']}'s Cunning"
        )

        if new_card['Cunning'] is None:
            return

        cards.append(new_card)

        easygui.msgbox(
            msg=f"\nName: {new_card['Name']}\n"
                f"Strength: {new_card['Strength']}\n"
                f"Speed: {new_card['Speed']}\n"
                f"Stealth: {new_card['Stealth']}\n"
                f"Cunning: {new_card['Cunning']}",
            title="Card added successfully"
        )


# Function for deleting a card
def delete_card():
    while True:
        card_delete = easygui.enterbox(
            msg="Type the name of the card you want to delete "
                "(use capitals where necessary).\n\n"
                "To go back to the option's menu, select 'Cancel.'",
            title="Delete Card"
        )

        if card_delete is None:
            return

        delete_card = None
        for card in cards:
            if card['Name'] == card_delete:
                delete_card = card
                break

        if delete_card:
            easygui.msgbox(
                msg=f"\nBelow are the stats of {delete_card['Name']}, the card you are about delete.\n"
                    f"\nName: {delete_card['Name']}\n"
                    f"Strength: {delete_card['Strength']}\n"
                    f"Speed: {delete_card['Speed']}\n"
                    f"Stealth: {delete_card['Stealth']}\n"
                    f"Cunning: {delete_card['Cunning']}",
                title=f"{delete_card['Name']}'s stats"
            )

            confirm_delete = easygui.buttonbox(
                msg=f"\nAre you sure want to delete {delete_card['Name']}?",
                choices=["Yes", "No"], title="Confirm Deletion"
            )

            if confirm_delete == "Yes":
                cards.remove(delete_card)
                easygui.msgbox(
                    msg=f"{delete_card['Name']} has been deleted.",
                    title=f"{delete_card['Name']} Deleted"
                )
        else:
            easygui.msgbox(msg="\nCard not found", title="Error")


# Main routine
easygui.msgbox("***Welcome to Monster Cards!***")
name = easygui.enterbox("Please enter your name: ")
easygui.msgbox(f"Welcome to the Monster Cards, {name}!")
played_before = yes_no(
    "Have you used 'Monster Cards' before?\n"
    "(Select 'Yes' to go to the option's menu.\n"
    "Select 'No' to view the instructions.)"
)

if played_before == "No":
    instructions()

while True:
    option = easygui.buttonbox(
        msg="What would you like to do?", title="Option's Menu",
        choices=["Display Instructions", "Output Cards", "Search and Edit Cards",
                 "Add Card", "Delete Card", "Exit"]
    )

    if option == "Display Instructions":
        instructions()

    elif option == "Output Cards":
        output_cards()

    elif option == "Search and Edit Cards":
        search_and_edit()

    elif option == "Add Card":
        add_card()

    elif option == "Delete Card":
        delete_card()

    elif option == "Exit":
        break
