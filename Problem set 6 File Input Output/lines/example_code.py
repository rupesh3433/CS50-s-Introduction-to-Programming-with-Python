import random

#program to check, that random num is less, more, or equal to 5
random_num = random.randint(1, 10)
if random_num > 5:
    print("Greater than 5")
elif random_num < 5:
    print("Less than 5")
    """
    this is multi line comments
    you can write many lines inside here
    these lines inside triple quotes should not be counted while counting number of lines
    """
else:
    print("Equal to 5")
