"""00_monster_cards_base_v1.
This is the first version of the base code for Monster Game.
For each of the versions for these, I will add finished components to
the option's menu. In this version of the base code, I have added the
Option's Menu and the welcome message to the program. For now, the
Option's Menu is empty besides an option to exit the program."""


import easygui

# Welcome Message
easygui.msgbox("---Welcome to Monster Cards!---")
# Asks for name
name = easygui.enterbox("Please enter your name: ")
# Combines welcome message and name
easygui.msgbox(f"Welcome to the Monster Cards, {name}!")


while True:
    option = easygui.buttonbox(msg="What would you like to do?", title="Option's Menu",
                               choices=["Exit"])

    if option == "Exit":
        break
