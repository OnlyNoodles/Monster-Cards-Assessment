"""02_instructions_v1.
Added instructions to 01_yes_no_checker_v7."""

import easygui


# Yes/no checker function
def yes_no(question_text):
    # Ask the user if they have played before
    answer = easygui.buttonbox(msg=question_text, choices=["Yes", "No"], title="Been Here Before?")

    # If user says 'Yes' or 'No', return their answer
    return answer


# Main routine
played_before = yes_no("Have you used 'Monster Cards' before?\n"
                       "(Select 'Yes' to go to the option's menu.\n "
                       "Select 'No' to view the instructions.)")

if played_before == "No":
    easygui.msgbox(msg="To output the all cards to the Python console, select 'Output Cards.'\n"
                       "To search for a card, select 'Search and Edit Cards.'"
                       "Selecting this will also give you a choice to edit the card"
                       "you have searched for, such as its name and stats.\n"
                       "To add a card, select 'Add Card.'\n"
                       "To delete a card, select 'Delete Card.'\n"
                       "To exit 'Monster Cards,' select 'Exit.'", title="Instructions")
