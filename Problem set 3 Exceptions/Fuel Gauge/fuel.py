def main():
    result = get_result()
    if result != -1:
        if result <= 1:
            print("E")
        elif result >= 99:
            print("F")
        else:
            print(f"{result}%")


def get_result():
    while True:
        try:
            expression = input("Fraction: ").strip()
            num1, num2 = expression.split("/")
            x = int(num1)
            y = int(num2)
            if x > y:
                pass
            else:
                return round((x / y)*100)
        except (ValueError, ZeroDivisionError):
            pass

main()
