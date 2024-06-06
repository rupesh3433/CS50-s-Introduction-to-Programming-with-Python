
input_twits = input("Input: ").strip()
output_twits = ""

vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
for letter in input_twits:
    if letter in vowel:
        continue
    else:
        output_twits += letter
print(f"Output: {output_twits}")
