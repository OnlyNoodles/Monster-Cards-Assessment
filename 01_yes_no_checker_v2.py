"""01_yes_no_checker_v2.
Put the function into a while loop so that the program
will repeatedly ask the user for a valid response when they
enter an invalid response. Doing this also makes testing
more efficient and easier, and also simplifies the user's input
by converting it to lowercase."""

show_instructions = ""
while show_instructions != "x":

    # Ask the user if they have played before
    show_instructions = input("Have you used 'Monster Cards' before?: ").lower()

    # If they say yes, output 'Program Continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # If they say no, output 'Display Instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    # Otherwise - show error
    else:
        print("Please answer 'Yes' or 'No'")

    print(f"You entered '{show_instructions}'")
