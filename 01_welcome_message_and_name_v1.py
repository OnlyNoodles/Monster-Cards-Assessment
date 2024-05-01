"""01_welcome_message_and_name_v1.
This is the first bit of the program that the user will see,
except it won't be this version. This little part will
welcome the user and ask for the user's name."""

# Welcome Message
print("---Welcome to Monster Cards!---")
print()
# Asks for name
name = input("Please enter your name: ")
print()
# Combines welcome message and name
print(f"Welcome to the Monster Cards, {name}!")
