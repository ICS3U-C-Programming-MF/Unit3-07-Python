#!usr/bin/env python3
# Made by Maximiliano Fairman
# Created on oct 20th 2025
# This program will only approve of you dating
# if you are either rich OR really good looking.


def main():

    # Ask the user if they are good looking
    good_looking = input("Are you good looking? (yes/no): ").strip().lower()

    # Ask the user if they are rich
    rich = input("Are you rich? (yes/no): ").strip().lower()

    # Check for invalid input first
    if good_looking not in ["yes", "no"] or rich not in ["yes", "no"]:
        print("Invalid input. Please answer with 'yes' or 'no'.")

        return  # stop the program here so it doesn't print other messages

    # If answers are good deside weather
    # to approve or not
    if good_looking == "yes" or rich == "yes":
        print("You are approved to date!")
    else:
        print("You are not approved to date.")


# End of program
if __name__ == "__main__":
    main()
