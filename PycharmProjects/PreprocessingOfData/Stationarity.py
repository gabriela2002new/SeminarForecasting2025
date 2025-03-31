import datetime
import random


def main():
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ask user for their name
    name = input("What's your name? ")

    # Generate a random number
    random_number = random.randint(1, 100)

    # Print messages
    print(f"Hello, {name}!")
    print(f"The current date and time is: {current_date}")
    print(f"Here's a random number for you: {random_number}")


# Run the main function
if __name__ == "__main__":
    main()
