expression = input("Expression: ").strip()

add_index = expression.find('+')
subtract_index = expression.find('-')
multiply_index = expression.find('*')
divide_index = expression.find('/')

index = 0

if add_index != -1:
    index = add_index
elif subtract_index != -1:
    index = subtract_index
elif multiply_index != -1:
    index = multiply_index
elif divide_index != -1:
    index = divide_index

num1 = int(expression[:index-1])
num2 = int(expression[index+2:])

sign = expression[index:index+1]

if sign == '+':
    print(float(num1 + num2))
elif sign == '-':
    print(float(num1 - num2))
elif sign == '*':
    print(float(num1 * num2))
elif sign == '/':
    print(float(num1 / num2))
