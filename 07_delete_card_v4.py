"""07_delete_card_v4.
Turned 07_delete_card_v3 into a function.
Changed variable names so that 'delete_card'
is not used for the name of the variable and the function.
Added titles for all easygui boxes. This
is the version I will use in 00_monster_cards_v6."""

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


delete_card()
