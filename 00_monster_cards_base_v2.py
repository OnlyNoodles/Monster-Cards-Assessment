"""00_monster_cards_base_v2.
Added the 'Yes/No Checker' function to the 00_monster_cards_v1
 along with the 'Instructions' function to the main
 routine and the option's menu in case the user forgets
 how to use the program and wants to read about how
 to use it again."""


import easygui


# Yes/no checker function
def yes_no(question_text):
    # Ask the user if they have played before
    answer = easygui.buttonbox(msg=question_text, choices=["Yes", "No"])

    # If they say yes or no, return their answer
    return answer


# Instructions function
def instructions():
    easygui.msgbox(msg="To view the instructions again, select 'Display Instructions.'\n"
                       "To output the all cards to the Python console, select 'Output Cards.'\n"
                       "To search for a card, select 'Search Cards.'\n"
                       "To add a card, select 'Add Card.'\n"
                       "To delete a card, select 'Delete Card.'\n"
                       "To exit 'Monster Cards,' select 'Exit.'", title="Instructions")


# Main routine

# Welcome Message
easygui.msgbox("*** Welcome to Monster Cards! ***")
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
                               choices=["Display Instructions", "Exit"])

    if option == "Display Instructions":
        instructions()

    elif option == "Exit":
        break
        