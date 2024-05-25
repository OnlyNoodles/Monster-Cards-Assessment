"""00_monster_cards_base_v4.
Added the 'Search Cards' function to 00_monster_cards_v3
and to the option's menu."""


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
    easygui.msgbox(msg="To view the instructions again, select 'Display Instructions.'\n"
                       "To output the all cards to the Python console, select 'Output Cards.'\n"
                       "To search for a card, select 'Search Card.'\n"
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


def search():
    # Ask the user for what combo they want to search
    card_search = easygui.enterbox(msg="Type the name of the card you want to search for "
                                       "(use capitals where necessary).\n"
                                   "To go back to the option's menu, enter 'Cancel.'", title="Search Card")

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


# Main routine

# Welcome Message
easygui.msgbox("---Welcome to Monster Cards!---")
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
                               choices=["Display Instructions", "Output Cards", "Search Card", "Exit"])

    if option == "Display Instructions":
        instructions()

    elif option == "Output Cards":
        output()

    elif option == "Search Card":
        search()

    elif option == "Exit":
        break
        