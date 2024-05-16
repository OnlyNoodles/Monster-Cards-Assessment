"""01_yes_no_checker_v2.
Tur ned 03_yes_no_checker_v3 into a function."""


import easygui


# Functions go here...
def yes_no(question_text):
    # Ask the user if they have played before
    answer = easygui.buttonbox(msg=question_text, choices=["Yes", "No"])

    # If they say yes, output 'Program Continues'
    if answer == "Yes":
        return answer

    # If they say no, output 'Display Instructions'
    elif answer == "No":
        return answer

    easygui.msgbox(f"You entered '{answer}'")


# Function to display instructions
def instructions():
    print("**** How To Play ****")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# Main routine goes here...
played_before = easygui.msgbox(yes_no("Have you used 'Monster Cards' before?: "))


if played_before == "No":
    instructions()
else:
    print("Program continues")
