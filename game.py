import random

MOVES = ["R", "P", "S"]

if __name__ == "__main__":
    print("This is Rock, Paper, Scissors game. Input R, P, or S, capital or small, and see who wins!\n")

    try:
        while True:
            user_input = input("Enter R, P, or S (or Q to quit): ").strip().upper()
            if user_input == "Q":
                print("Goodbye!")
                break

            if user_input not in MOVES:
                print("Invalid input. Input R, P, or S, capital or small")
                continue

            computer_choice = random.choice(MOVES)

            match(user_input, computer_choice):
                case ("R", "S") | ("P", "R") | ("S", "P"):
                    print(f"You chose {user_input}, computer chose {computer_choice}. You win!")
                case ("S", "R") | ("R", "P") | ("P", "S"):
                    print(f"You chose {user_input}, computer chose {computer_choice}. You lose!")
                case _:
                    print(f"You both chose {user_input}. It's a tie!")

    except KeyboardInterrupt:
        print("\nGoodbye!")
