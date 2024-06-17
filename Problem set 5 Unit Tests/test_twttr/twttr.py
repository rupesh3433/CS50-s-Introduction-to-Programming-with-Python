def main():
    input_twits = input("Input: ").strip()
    print(f"Output: {shorten(input_twits)}")

def shorten(input_twits):
    vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    #MY LOGIC
    output_twits = ""
    for letter in input_twits:
        if letter in vowel:
            continue
        else:
            output_twits += letter
    return output_twits

    #ALTERNATIVE WAY
    # return ''.join([char for char in input_twits if char not in vowel])

if __name__ == "__main__":
    main()
