import random

def roll_dice(num_dice=1):
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (or 0 to exit): "))
            if num_dice == 0:
                print("Exiting the Dice Rolling Simulator. Goodbye!")
                break
            elif num_dice < 0:
                print("Please enter a positive number.")
            else:
                results = roll_dice(num_dice)
                print(f"Rolling {num_dice} dice: {results}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()