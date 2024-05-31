"""00_monster_cards_base_v2.
Added the 'Yes/No Checker' function to the 00_monster_cards_v1
 along with the 'Instructions' function to the main
 routine and the option's menu in case the user forgets
 how to use the program and wants to read about how
 to use it again."""


import easygui


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


# Main routine

# Welcome Message
easygui.msgbox("*** Welcome to Monster Cards! ***")
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
                               choices=["Display Instructions", "Exit"])

    # If user selects 'Display Instructions,' run instructions() function
    if option == "Display Instructions":
        instructions()

    # If user selects 'Exit,' exit the program
    elif option == "Exit":
        break
