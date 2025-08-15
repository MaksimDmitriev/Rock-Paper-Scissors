import random
import time
from enum import Enum

MODES = ["C", "U"]
MOVES = ["R", "P", "S"]


class Outcome(Enum):
    WIN = "WIN"
    LOSE = "LOSE"
    TIE = "TIE"


def play_with_computer():
    while True:
        user_input = input("Enter R, P, or S (or Q to quit): ").strip().upper()
        if user_input == "Q":
            print("Goodbye!")
            break

        if user_input not in MOVES:
            print("Invalid input. Input R, P, or S, capital or small")
            continue

        computer_choice = random.choice(MOVES)

        match get_game_result(user_input, computer_choice):
            case Outcome.WIN:
                print(f"You chose {user_input}, computer chose {computer_choice}. You win!")
            case Outcome.LOSE:
                print(f"You chose {user_input}, computer chose {computer_choice}. You lose!")
            case _:
                print(f"You both chose {user_input}. It's a tie!")


def watch_computer_playing():
    while True:
        computer_choice1 = random.choice(MOVES)
        computer_choice2 = random.choice(MOVES)
        time.sleep(1)
        match get_game_result(computer_choice1, computer_choice2):
            case Outcome.WIN:
                print(f"Computer 1 chose {computer_choice1}, Computer 2 chose {computer_choice2}. Computer 1 wins!")
            case Outcome.LOSE:
                print(f"Computer 1 chose {computer_choice1}, Computer 2 chose {computer_choice2}. Computer 2 wins!")
            case _:
                print(f"Both computers chose {computer_choice1}. It's a tie!")


def get_game_result(first_input, second_input):
    if first_input == second_input:
        return Outcome.TIE
    elif (first_input == "R" and second_input == "S") or \
            (first_input == "P" and second_input == "R") or \
            (first_input == "S" and second_input == "P"):
        return Outcome.WIN
    else:
        return Outcome.LOSE


if __name__ == "__main__":
    try:
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
    except KeyboardInterrupt:
        print("\nGoodbye!")
