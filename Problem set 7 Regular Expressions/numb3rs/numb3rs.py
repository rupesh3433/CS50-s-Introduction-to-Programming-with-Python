import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern_255 = "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    full_pattern = rf"^{pattern_255}\.{pattern_255}\.{pattern_255}\.{pattern_255}$"
    matches = re.match(full_pattern, ip)
    if matches is None:
        return False
    for number in matches.groups():
        number = int(number)
        if number < 0 or number > 255:
            return False
    return True

if __name__ == "__main__":
    main()
