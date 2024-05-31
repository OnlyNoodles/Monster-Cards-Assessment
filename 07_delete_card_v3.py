"""07_delete_card_v3.
Edited 07_delete_card_v2 to that when the user selects 'Cancel'
when the program asks for a card to delete, the user can go back
to the option's menu. Added a confirmation message after deleting
a card."""

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
    # Asks the user to input an existing card they want to delete
    card_delete = easygui.enterbox("Type the name of the card you want to delete (use capitals where necessary).\n"
                                   "To go back to the option's menu, select 'Cancel.'")

    # # Exit the loop if 'Cancel' is selected
    if card_delete is None:
        break

    # Checks if the card exists
    delete_card = None
    for card in cards:
        if card['Name'] == card_delete:
            delete_card = card
            break

    # Display searched card
    if delete_card:
        # Sorts each stat for searched monster downwards without curly brackets or commas
        easygui.msgbox(f"\nBelow are the stats of {delete_card['Name']}, the card you are about delete.\n"
                       f"\nName: {delete_card['Name']}\n"
                       f"Strength: {delete_card['Strength']}\n"
                       f"Speed: {delete_card['Speed']}\n"
                       f"Stealth: {delete_card['Stealth']}\n"
                       f"Cunning: {delete_card['Cunning']}")

        while True:
            # Confirm with user if they want to delete
            confirm_delete = easygui.buttonbox(f"\nAre you sure want to delete {delete_card['Name']}?",
                                               choices=["Yes", "No"])

            # If user inputs 'Yes,' delete the card
            if confirm_delete == "Yes":
                cards.remove(delete_card)
                easygui.msgbox(f"{delete_card['Name']} has been deleted.")
                break

            # If user inputs 'No,' break
            elif confirm_delete == "No":
                break

    # Error message if user searches for a card or anything not from the list
    else:
        easygui.msgbox("\nCard not found")
