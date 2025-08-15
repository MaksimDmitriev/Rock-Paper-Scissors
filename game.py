import random
import time

MODES = ["C", "U"]
MOVES = ["R", "P", "S"]


def play_with_computer():
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

            match (user_input, computer_choice):
                case ("R", "S") | ("P", "R") | ("S", "P"):
                    print(f"You chose {user_input}, computer chose {computer_choice}. You win!")
                case ("S", "R") | ("R", "P") | ("P", "S"):
                    print(f"You chose {user_input}, computer chose {computer_choice}. You lose!")
                case _:
                    print(f"You both chose {user_input}. It's a tie!")

    except KeyboardInterrupt:
        print("\nGoodbye!")


def watch_computer_playing():
    try:
        while True:
            computer_choice1 = random.choice(MOVES)
            computer_choice2 = random.choice(MOVES)
            time.sleep(1)
            match (computer_choice1, computer_choice2):
                case ("R", "S") | ("P", "R") | ("S", "P"):
                    print(f"Computer 1 chose {computer_choice1}, Computer 2 chose {computer_choice2}. Computer 1 wins!")
                case ("S", "R") | ("R", "P") | ("P", "S"):
                    print(f"Computer 1 chose {computer_choice1}, Computer 2 chose {computer_choice2}. Computer 2 wins!")
                case _:
                    print(f"Both computers chose {computer_choice1}. It's a tie!")
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    game_mode = input(
        "Enter C to watch the computer playing with itself or U to play with the computer: ").strip().upper()
    while True:
        if game_mode in MODES:
            break
        print("Invalid input. Input C or U, capital or small")

    if game_mode == "C":
        print("Computer will play with itself")
        watch_computer_playing()
    elif game_mode == "U":
        print("This is Rock, Paper, Scissors game. Input R, P, or S, capital or small, and see who wins!\n")
        play_with_computer()
