# CS50's Introduction to Programming with Python

Welcome to CS50's Introduction to Programming with Python! This repository contains solutions to various programming challenges presented in the course. Each problem set is outlined below along with a brief explanation of what each program does.

## Problem Set 0

### [Indoor Voice](Problem%20set%200%20Functions%20and%20Variables/Indoor%20Voice/indoor.py)

**Description:** This program converts input text to lowercase while preserving punctuation and whitespace.

**File:** `indoor.py`

This program takes input text and converts it to lowercase, ensuring that any punctuation and whitespace remain unchanged.

### [Playback Speed](Problem%20set%200%20Functions%20and%20Variables/Playback%20Speed/playback.py)

**Description:** This program replaces spaces in input text with three periods, mimicking a slower playback speed.

**File:** `playback.py`

The program replaces spaces in the input text with three periods, creating a visual effect similar to slowing down the playback speed.

### [Making Faces](Problem%20set%200%20Functions%20and%20Variables/Making%20Faces/faces.py)

**Description:** This program converts emoticons in input text to corresponding emojis.

**File:** `faces.py`

The program scans the input text for emoticons like ":)" and ":(" and replaces them with corresponding emojis, such as "🙂" and "🙁".

### [Einstein](Problem%20set%200%20Functions%20and%20Variables/Einstein/einstein.py)

**Description:** This program calculates the energy equivalent of mass using Einstein's famous formula, E=mc².

**File:** `einstein.py`

The program prompts the user to input mass (in kilograms) and then calculates the equivalent energy in joules using the formula E=mc², where 'c' is the speed of light.

### [Tip Calculator](Problem%20set%200%20Functions%20and%20Variables/Tip%20Calculator/tip.py)

**Description:** This program calculates the tip amount based on the meal cost and tip percentage.

**File:** `tip.py`

This program calculates the tip amount for a given meal cost and tip percentage provided by the user.



## Problem Set 1

### [Deep Thought](Problem%20set%201%20Conditionals/Deep%20Thought/deep.py)

**Description:** This program prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting "Yes" if the user inputs "42" or (case-insensitively) "forty-two" or "forty two". Otherwise, it outputs "No".

**File:** `deep.py`

In deep.py, the program asks the user for the answer to the Great Question of Life, the Universe and Everything and responds based on the provided input.

### [Home Federal Savings Bank](Problem%20set%201%20Conditionals/Home%20Federal%20Savings%20Bank/bank.py)

**Description:** This program prompts the user for a greeting. If the greeting starts with "hello", it outputs $0. If the greeting starts with an "h" (but not "hello"), it outputs $20. Otherwise, it outputs $100.

**File:** `bank.py`

In bank.py, the program checks the user's greeting and outputs an amount based on whether the greeting starts with "hello", an "h", or anything else.

### [File Extensions](Problem%20set%201%20Conditionals/File%20Extensions/extensions.py)

**Description:** This program prompts the user for the name of a file and then outputs that file’s media type based on its extension. If the file has an unrecognized or missing extension, it outputs "application/octet-stream".

**File:** `extensions.py`

In extensions.py, the program maps file extensions to their corresponding media types and outputs the appropriate type based on the user's input.

### [Math Interpreter](Problem%20set%201%20Conditionals/Math%20Interpreter/interpreter.py)

**Description:** This program prompts the user for an arithmetic expression formatted as "x y z", with one space between x and y and one space between y and z, and then calculates and outputs the result as a floating-point value formatted to one decimal place.

**File:** `interpreter.py`

In interpreter.py, the program interprets simple arithmetic expressions and outputs the result, formatted to one decimal place.

### [Meal Time](Problem%20set%201%20Conditionals/Meal%20Time/meal.py)

**Description:** This program prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, it outputs nothing. Time is input in 24-hour format.

**File:** `meal.py`

In meal.py, the program checks the input time and determines if it falls within breakfast, lunch, or dinner time ranges, outputting the corresponding meal time.


## Problem Set 2

### [camelCase](Problem%20set%202%20Loops/Camel%20Case/camel.py)

**Description:** This program converts camel case variable names into snake case.

**File:** `camel.py`

The program prompts the user for a variable name in camel case and outputs the corresponding name in snake case. For example, `firstName` becomes `first_name`.

### [Coke Machine](Problem%20set%202%20Loops/Coke%20Machine/coke.py)

**Description:** This program simulates a Coke vending machine, accepting coins and calculating change.

**File:** `coke.py`

The program prompts the user to insert coins (25 cents, 10 cents, or 5 cents) until the total reaches or exceeds 50 cents. It then outputs how much change is owed.

### [Just setting up my twttr](Problem%20set%202%20Loops/Twttr/twttr.py)

**Description:** This program removes vowels from the input text.

**File:** `twttr.py`

The program prompts the user for a string of text and outputs that same text but with all vowels (A, E, I, O, and U) removed, whether they are in uppercase or lowercase.

### [Vanity Plates](Problem%20set%202%20Loops/Vanity%20Plates/plates.py)

**Description:** This program validates vanity license plates based on specific rules.

**File:** `plates.py`

The program prompts the user for a vanity plate and checks if it meets the following criteria:
- It starts with at least two letters.
- It contains a maximum of 6 characters and a minimum of 2 characters.
- Numbers, if used, must be at the end and cannot start with '0'.
- No periods, spaces, or punctuation marks are allowed.

It outputs "Valid" if all conditions are met, otherwise "Invalid".

### [Nutrition Facts](Problem%20set%202%20Loops/Nutrition%20Facts/nutrition.py)

**Description:** This program outputs the number of calories for a given fruit.

**File:** `nutrition.py`

The program prompts the user to input the name of a fruit (case-insensitively) and outputs the number of calories in one portion of that fruit, based on the FDA's nutrition facts. If the fruit is not in the list, it outputs nothing.

## Feel free to explore each problem set, run the programs, and modify them as needed!

