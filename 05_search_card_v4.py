# List of cards
import easygui

cards = [{"Name": "Stoneling", "Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
         {"Name": "Vexscream", "Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
         {"Name": "Dawnmirage", "Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
         {"Name": "Blazegolem", "Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
         {"Name": "Websnake", "Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
         {"Name": "Moldvine", "Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
         {"Name": "Vortexwing", "Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
         {"Name": "Rotthing", "Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
         {"Name": "Froststep", "Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
         {"Name": "Whispghoul", "Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}]


# Function for number checker
def number_checker(question):
    while True:
        try:
            value = float(input(question))
            if 1 <= value <= 25:
                return value
            else:
                print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Please enter a number between 1 and 25.")


# Ask the user for what combo they want to search
card_search = easygui.enterbox("Type the name of the card you want to search for (use capitals where necessary): ")

# Checks if card exists
found_card = None
for card in cards:
    if card['Name'] == card_search:
        found_card = card
        break

# Display result
if found_card:
    # Sorts each stat for searched monster downwards without curly brackets or commas
    easygui.msgbox(msg=f"\nName: {found_card['Name']}\n"
                       f"Strength: {found_card['Strength']}\n"
                       f"Speed: {found_card['Speed']}\n"
                       f"Stealth: {found_card['Stealth']}\n"
                       f"Cunning: {found_card['Cunning']}",
                   title=found_card['Name'])
    # Ask the user if they want to edit the card
    edit_choice = easygui.buttonbox(msg="Do you want to edit this card?", choices=["Yes", "No"])
    if edit_choice == "Yes":
        while True:
            stat_to_edit = easygui.buttonbox(msg="Which stat do you want to edit?",
                                             choices=['Name', 'Strength', 'Speed', 'Stealth', 'Cunning'])

            if stat_to_edit == 'Name':
                new_name = easygui.enterbox(f"Enter the new name for the monster")
                found_card['Name'] = new_name
                easygui.msgbox(f"Name has been updated to {new_name}.")
                break

            elif stat_to_edit in ['Strength', 'Speed', 'Stealth', 'Cunning']:
                new_value = number_checker(f"Enter the new value for {stat_to_edit} (1-25): ")
                found_card[stat_to_edit] = new_value
                easygui.msgbox(f"{stat_to_edit} has been updated to {new_value}.")
                break

        # Display updated card
        print("\nUpdated card:")
        print(f"Name: {found_card['Name']}")
        print(f"Strength: {found_card['Strength']}")
        print(f"Speed: {found_card['Speed']}")
        print(f"Stealth: {found_card['Stealth']}")
        print(f"Cunning: {found_card['Cunning']}")

else:
    print("\nCard not found")
