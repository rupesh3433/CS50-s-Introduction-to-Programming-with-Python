import random
import sys

def main():
    level = taking_level_input()
    random_num = random.randint(1,level)
    prompt_user_to_guess(random_num)


def taking_level_input():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def prompt_user_to_guess(random_num):
    while True:
        try:
            guessed_num = int(input("Guess: "))
            if guessed_num > 0:
                if guessed_num > random_num:
                    print("Too large!")
                elif guessed_num < random_num:
                    print("Too small!")
                else:
                    sys.exit("Just right!")
        except ValueError:
            pass

main()
