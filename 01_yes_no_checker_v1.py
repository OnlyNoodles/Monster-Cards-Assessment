"""01_yes_no_checker_v1.
This is the first version of the Yes/No Checker.
It is the first component that the user will experience
in the program as it will ask the user of they have used
this program before and if not, it will display the
instructions component."""

# Ask the user if they have played before
show_instructions = input("Have you used 'Monster Cards' before? :")

# If they say yes, output 'Program Continues'
if show_instructions == "yes":
    print("Program continues")

# If they say no, output 'Display Instructions'
elif show_instructions == "no":
    print("Display instructions")

# Otherwise - show error
else:
    print("Please answer 'Yes' or 'No'")
