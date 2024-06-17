def main():
    greeting = input("Greeting: ").strip()
    result = value(greeting)
    print(f"${result}")

#check if there is "hello" in greeting or not.
def value(greeting):
    greeting = greeting.lower()
    if "hello" in greeting:
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
