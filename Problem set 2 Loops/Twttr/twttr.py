def main():
    input_twits = input("Input: ").strip()
    print(f"Output: {shorten(input_twits)}")

def shorten(input_twits):
    output_twits = ""
    vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for letter in input_twits:
        if letter in vowel:
            continue
        else:
            output_twits += letter
    return output_twits

if __name__ == "__main__":
    main()
