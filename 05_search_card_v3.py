"""05_search_cards_v3.
Turned 02_search_card_v2 into a function"""

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


def search():
    # Ask the user for what combo they want to search
    card_search = easygui.enterbox(msg="Type the name of the card you want to search for "
                                       "(use capitals where necessary).\n"
                                   "To go back to the option's menu, enter 'Cancel.'"
                                       "Cards are ", title="Search Card")

    # Returns user to option's menu if user selects 'Cancel'
    if card_search is None or card_search == "Cancel":
        return

    # Checks if card exists
    found_card = None
    for card in cards:
        if card['Name'] == card_search:
            found_card = card
            break

    # Display result
    if found_card:
        # Sorts each stat for searched monster downwards without curly brackets or commas
        easygui.msgbox(msg=f"\nName: {found_card['Name']}\n"
                           f"Strength: {found_card['Strength']}\n"
                           f"Speed: {found_card['Speed']}\n"
                           f"Stealth: {found_card['Stealth']}\n"
                           f"Cunning: {found_card['Cunning']}",
                       title=found_card['Name'])

    else:
        easygui.msgbox(msg="\nCard not found", title="Card not found")


search()
