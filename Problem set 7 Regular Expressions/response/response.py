from validator_collection import checkers

def main():
    print(is_valid_email(input("What's your email address? ").strip()))

def is_valid_email(email_address):
    if checkers.is_email(email_address):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
