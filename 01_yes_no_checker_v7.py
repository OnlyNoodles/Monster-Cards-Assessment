"""01_yes_no_checker_v7.
Made the Yes/No Checker function from 01_yes_no_checker_v6
even shorter by only putting the easygui.buttonbox() in it.
As for the question and the 'if' statements, I have moved
those to the main routine. This will allow for 'Yes'
to take the user to the option's menu. This is the version
I will use in 00_monster_cards_base_v2 and future versions
of 00_monster_cards_base."""

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

# Display Instructions if user selects 'No'
if played_before == "No":
    easygui.msgbox(msg="Display instructions", title="Display Instructions")
