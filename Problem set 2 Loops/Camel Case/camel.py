
camelCase = input("camelCase: ").strip()
snake_Case = ""

index = -1
prev_counter = 0
for letter in camelCase:
    index += 1
    if ord(letter) >= 65 and ord(letter) <= 90:
        snake_Case += camelCase[prev_counter:index]
        snake_Case += "_"
        prev_counter = index
snake_Case += camelCase[prev_counter:index+1]
snake_Case = snake_Case.lower()
print(snake_Case)
