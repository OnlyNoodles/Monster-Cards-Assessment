"""00_monster_cards_base_v1.
This is the first version of the base code for Monster Game.
For each of the versions for these, I will add finished components to
the option's menu. The first component I have added here, along with
implementing an option's menu, is the welcome message and name
function (01_welcome_message_and_name_v2)."""


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
        