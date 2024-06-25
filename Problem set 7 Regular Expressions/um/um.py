import re


def main():
    print(count(input("Text: ")))

def count(s):
    # " \b " --> It is a word boundry which assures that "um" is not a substring. It is complete word
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    if matches:
        return len(matches)
    return 0

if __name__ == "__main__":
    main()
