print("Welcome to the Voter Registration App")

name = input("\nPlease enter your name: ").title()
age = int(input("Please enter your age: "))

if age < 18:
    print("\nYou are not old enough to register to vote.")

if age >= 18:
    print(f"""\nCongratulations {name}! You are old enough to register to vote.
    Here is a list of political parties to join.\n\t- Republican\n\t- Democratic\n\t- Independent\n\t- Libertarian\n\t- Green
    """)
partido = input("\nWhat party would you like to join: ").title()

print(f"Congratulations Mike! You have joined the {partido} party! \nThat is a major party!")


