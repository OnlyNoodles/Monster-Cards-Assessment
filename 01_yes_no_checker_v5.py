"""01_yes_no_checker_v5.
Added easygui into 01_yes_no_checker_v5."""

import easygui


# Functions go here...
def yes_no(question_text):
    while True:
        # Ask the user if they have played before
        answer = easygui.enterbox(msg=question_text,
                                  title="Have you been here before?")

        # If they say yes, output 'Program Continues'
        if answer == "Yes":
            easygui.msgbox("Program continues")
            break

        elif answer == "Y":
            easygui.msgbox("Program continues")
            break

        elif answer == "y":
            easygui.msgbox("Program continues")
            break

        # If they say no, output 'Display Instructions'
        elif answer == "No":
            easygui.msgbox("Display instructions")
            break

        elif answer == "N":
            easygui.msgbox("Display instructions")
            break

        elif answer == "n":
            easygui.msgbox("Display instructions")
            break

        else:
            easygui.msgbox("Please enter either 'Yes' or 'No'")

    easygui.msgbox(f"You entered '{answer}'")


# Main routine goes here...
show_instructions = easygui.msgbox(yes_no("Have you used 'Monster Cards' before?"))
