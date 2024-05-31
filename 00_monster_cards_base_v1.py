"""00_monster_cards_base_v1.
This is the first version of the base code for Monster Game.
For each of the versions for these, I will add finished components to
the option's menu. In this version of the base code, I have added the
Option's Menu and a welcome message to the program. For now, the
Option's Menu is empty besides an option to exit the program."""


import easygui

# Welcome Message
easygui.msgbox("*** Welcome to Monster Cards! ***")
# Asks for name
name = easygui.enterbox("Please enter your name: ")
# Combines welcome message and name
easygui.msgbox(f"Welcome to the Monster Cards, {name}!")

# Loop for option's menu so that it keeps re-asking the question after every function until the user exits
while True:
    # Ask the user what they want to do
    option = easygui.buttonbox(msg="What would you like to do?", title="Option's Menu",
                               choices=["Exit"])

    # If user selects 'Exit,' exit the program
    if option == "Exit":
        break
