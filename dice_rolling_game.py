# Import the random mode
import random

# A while loop to ensure the game can continue running
while True:

    option = input("Roll the dice? (y/n): ")

    if option.lower() == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f" {die1}, {die2}")

    elif option.lower() == "n":
        print("Thank you for playing")
        break

    else:
        print("Invalid choice!")

