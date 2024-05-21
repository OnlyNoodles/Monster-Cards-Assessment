"""01_yes_no_checker_v2.
Turned 03_yes_no_checker_v3 into a function."""


import easygui


# Functions go here...
def yes_no(question_text):
    # Ask the user if they have played before
    answer = easygui.buttonbox(msg=question_text, choices=["Yes", "No"])

    # If they say yes or no, return their answer
    return answer


# Function to display instructions
def instructions():
    easygui.msgbox(msg="To output the all cards to the Python console, select 'Output Cards.'\n"
                       "To search for a card, select 'Search Cards.'\n"
                       "To add a card, select 'Add Card.'\n"
                       "To delete a card, select 'Delete Card.'\n"
                       "To exit 'Monster Cards,' select 'Exit.'", title="Instructions")


# Main routine goes here...
played_before = yes_no("Have you used 'Monster Cards' before?")

if played_before == "No":
    instructions()
else:
    easygui.msgbox("Program continues")
