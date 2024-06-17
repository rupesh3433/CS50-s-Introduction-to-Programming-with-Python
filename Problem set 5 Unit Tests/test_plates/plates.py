def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (
        check_length(s) and
        check_start_with_letters(s) and
        check_valid_characters(s) and
        check_number_placement(s)
    )

def check_length(s):
    # Check if the plate length is between 2 and 6 characters
    return 2 <= len(s) <= 6

def check_start_with_letters(s):
    # Check if the plate starts with at least two letters
    return s[0:2].isalpha()

def check_valid_characters(s):
    # Check if all characters are alphanumeric
    return s.isalnum()

def check_number_placement(s):
    # Check if numbers are placed correctly
    found_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not found_number:
                # First number should not be '0'
                if char == '0':
                    return False
                found_number = True
        elif found_number and char.isalpha():
            # Letters after numbers are not allowed
            return False
    return True

if __name__ == "__main__":
    main()
