"""01_yes_no_checker_v6.
Added an easygui buttonbox so that the user cannot make an error.
This means that I have gotten rid of the while loop and error
message, therefore making this component significantly smaller and cleaner."""

import easygui


# Functions go here...
def yes_no(question_text):
    # Ask the user if they have played before
    answer = easygui.buttonbox(msg=question_text,
                               title="Have You Been Here Before",
                               choices=["Yes", "No"])

    # If they say yes, output 'Program Continues'
    if answer == "Yes":
        easygui.msgbox("Program continues")

    # If they say no, output 'Display Instructions'
    elif answer == "No":
        easygui.msgbox("Display instructions")

    easygui.msgbox(f"You entered {answer}.")

    
# Main routine goes here...
show_instructions = easygui.msgbox(yes_no("Have you used 'Monster Cards' before?"))
