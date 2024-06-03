# HERE, a function called convert() that accepts a str1 as input and returns that same input with any :) converted to 🙂 and any :( converted to 🙁. All other text are returned unchanged.

def main():
    str1 = input()
    str2 = convert(str1)
    print(str2)

def convert(strr):
    strr = strr.replace(":)", "\U0001F642")
    strr = strr.replace(":(", "\U0001F641")
    return strr

main()
