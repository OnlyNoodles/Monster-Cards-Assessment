"""04_output_cards_v3.
Changed 04_output_cards_v2 into a function.
This is the version I will use in
00_monster_cards_base_v3 and the future
versions of 00_monster_cards_base."""

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


# Function for outputting cards
def output_cards():
    # Outputs the list of cards
    print("\n*** Monster names and stats ***")
    for monster in cards:
        # Sorts each stat for each monster downwards without curly brackets or commas
        print(f"\nName: {monster['Name']}")
        print(f"Strength: {monster['Strength']}")
        print(f"Speed: {monster['Speed']}")
        print(f"Stealth: {monster['Stealth']}")
        print(f"Cunning: {monster['Cunning']}")


output_cards()
