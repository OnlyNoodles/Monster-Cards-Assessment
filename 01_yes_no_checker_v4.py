"""01_yes_no_checker_v4.
Turned 03_yes_no_checker_v3 into a function."""


# Functions go here...
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer
        # Otherwise - show error
        else:
            print("Please answer 'Yes' or 'No'")

        print(f"You entered '{answer}'")


# Main routine goes here...
show_instructions = yes_no("Have you used 'Monster Cards' before?: ")
print(f"You entered '{show_instructions}'")
print()
