import random

def main():
    level = get_level()
    right_ans = generate_10_math_problems(level)
    print(f"Score: {right_ans}")

def get_level():
    while True:
        level = input("Level: ").strip()
        if level in {"1", "2", "3"}:
            return int(level)

def generate_10_math_problems(level):
    right_ans = 0
    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        if ask_question(num1, num2):
            right_ans += 1
    return right_ans

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

def ask_question(num1, num2):
    for _ in range(3):  # Give up to 3 attempts
        try:
            result = int(input(f"{num1} + {num2} = "))
            if result == (num1 + num2):
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"{num1} + {num2} = {num1 + num2}")
    return False

if __name__ == "__main__":
    main()
