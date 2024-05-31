"""02_instructions_v2.
Turned the instructions from 02_instructions_v1
into a function.
Added titles to every easygui box.
This is the version I will use in 00_monster_cards_v2
and future versions of 00_monster_cards_base."""


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
played_before = yes_no("Have you used 'Monster Cards' before?")

# Display Instructions if user selects 'No'
if played_before == "No":
    instructions()

# Program continues if user selects 'Yes'
else:
    easygui.msgbox(msg="Program continues", title="Program Continues")
