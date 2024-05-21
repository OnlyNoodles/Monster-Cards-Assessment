"""00_monster_cards_base_v3.
Added the 'Output Cards' function to 00_monster_cards_v2
and to the option's menu."""


import easygui


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
                       "To search for a card, select 'Search Cards.'\n"
                       "To add a card, select 'Add Card.'\n"
                       "To delete a card, select 'Delete Card.'\n"
                       "To exit 'Monster Cards,' select 'Exit.'", title="Instructions")


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
                               choices=["Display Instructions", "Output Cards", "Exit"])

    if option == "Display Instructions":
        instructions()

    elif option == "Output Cards":
        output()

    elif option == "Exit":
        break
        