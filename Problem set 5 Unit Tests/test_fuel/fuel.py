def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            rounded_integer = convert(fraction)
            string_result = gauge(rounded_integer)
            print(string_result)
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    try:
        num1, num2 = fraction.split("/")
        x = int(num1)
        y = int(num2)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        return round((x / y)*100)
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(rounded_integer):
    if rounded_integer <= 1:
        return "E"
    elif rounded_integer >= 99:
        return "F"
    return f"{rounded_integer}%"


if __name__ == "__main__":
    main()
