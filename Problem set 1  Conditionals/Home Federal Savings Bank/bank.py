
greeting = input("Greeting: ").strip().lower()

#check if there is "hello" in greeting or not.
if "hello" in greeting:
    print("$0")
elif greeting[0] == 'h':
    print("$20")
else:
    print("$100")

