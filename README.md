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







## Problem Set 3

### [Fuel Gauge](Problem%20set%203%20Exceptions/Fuel%20Gauge/fuel.py)

**Description:** This program prompts the user for a fraction, formatted as X/Y, and outputs the fuel level as a percentage rounded to the nearest integer. If 1% or less remains, it outputs "E" for empty. If 99% or more remains, it outputs "F" for full. It handles exceptions for invalid input.

**File:** `fuel.py`

In fuel.py, the program converts a fraction representing fuel level into a percentage and outputs either the percentage, "E" for empty, or "F" for full, handling any invalid input gracefully.

### [Felipe’s Taqueria](Problem%20set%203%20Exceptions/Felipe's%20Taqueria/taqueria.py)

**Description:** This program allows the user to place an order at Felipe's Taqueria, prompting for items until the user inputs control-d. It displays the total cost after each input, ignoring invalid items and handling exceptions for end of input.

**File:** `taqueria.py`

In taqueria.py, the program takes orders for items from Felipe's menu, calculates the total cost, and handles end-of-input exceptions, ensuring continuous order taking until the user finishes.

### [Grocery List](Problem%20set%203%20Exceptions/Grocery%20List/grocery.py)

**Description:** This program prompts the user for grocery items until the user inputs control-d, then outputs the grocery list in uppercase, sorted alphabetically, and prefixed with the count of each item.

**File:** `grocery.py`

In grocery.py, the program collects grocery items from the user, counts and sorts them alphabetically, and outputs the list in uppercase, handling exceptions for end of input.

### [Outdated](Problem%20set%203%20Exceptions/Outdated/outdated.py)

**Description:** This program prompts the user for a date in either MM/DD/YYYY or "Month D, YYYY" format and converts it to YYYY-MM-DD format. It handles invalid dates by prompting the user again.

**File:** `outdated.py`

In outdated.py, the program converts dates from US format to ISO 8601 format, ensuring correct handling and re-prompting for invalid dates.





## Problem Set 4

### [Emojize](Problem%20set%204%20Libraries/Emojize/emojize.py)

**Description:** This program prompts the user for a string in English and converts any codes or aliases for emojis into their corresponding emoji symbols.

**File:** `emojize.py`

This program takes a user input string containing emoji codes or aliases and outputs the string with the codes replaced by the actual emojis using the `emoji` module.

### [Frank, Ian and Glen’s Letters](Problem%20set%204%20Libraries/Figlet/figlet.py)

**Description:** This program outputs text in ASCII art using FIGlet fonts. The user can specify a font or use a random one.

**File:** `figlet.py`

The program prompts the user for text and prints it in a specified FIGlet font (or a random font if none is specified) using the `pyfiglet` module.

### [Adieu, Adieu](Problem%20set%204%20Libraries/Adieu/adieu.py)

**Description:** This program prompts the user for names, one per line, until the user inputs control-d, then bids farewell to those names in a grammatically correct format.

**File:** `adieu.py`

The program collects names from the user and outputs a farewell message, formatting the names correctly using the `inflect` module to handle the list formatting.

### [Guessing Game](Problem%20set%204%20Libraries/Guess%20Game/game.py)

**Description:** This program implements a number guessing game where the user must guess a randomly generated number within a specified range.

**File:** `game.py`

The program prompts the user to input a level to set the range (1 to level), generates a random number, and guides the user to guess the number, providing feedback on each guess.

### [Little Professor](Problem%20set%204%20Libraries/Little%20Professor/professor.py)

**Description:** This program generates math problems for the user to solve, providing feedback and tracking the user's score.

**File:** `professor.py`

The program prompts the user to choose a level of difficulty, generates ten addition problems, and allows up to three attempts per problem, displaying the correct answer if not solved within three tries.

### [Bitcoin Price Index](Problem%20set%204%20Libraries/Bitcoin%20Price%20Index/bitcoin.py)

**Description:** This program calculates the current cost of a specified number of Bitcoins in USD using the CoinDesk API.

**File:** `bitcoin.py`

The program takes the number of Bitcoins as a command-line argument, fetches the current Bitcoin price from the CoinDesk API, and calculates and outputs the total cost in USD, formatted to four decimal places.






# Problem Set 5

## 1. [Setting up my twttr](Problem%20set%205%20Unit%20Tests/test_twttr/)

### [twttr.py](Problem%20set%205%20Unit%20Tests/test_twttr/twttr.py)

Implementation of functions related to manipulating strings without vowels. Specifically, the `shorten` function removes all vowels (both uppercase and lowercase) from a given string and returns the modified string.

### [test_twttr.py](Problem%20set%205%20Unit%20Tests/test_twttr/test_twttr.py)

Unit tests for `twttr.py` to thoroughly test the `shorten` function. Includes multiple test cases to ensure correct handling of strings with vowels, mixed cases, and edge cases where no vowels exist.

## 2. [Home Federal Savings Bank](Problem%20set%205%20Unit%20Tests/test_bank/)

### [bank.py](Problem%20set%205%20Unit%20Tests/test_bank/bank.py)

Implementation of banking functions to determine values based on greetings. The `value` function evaluates a greeting string and returns:
- 0 if the greeting starts with "hello" (case insensitive),
- 20 if the greeting starts with "h" (but not "hello"),
- 100 otherwise (if neither condition is met).

### [test_bank.py](Problem%20set%205%20Unit%20Tests/test_bank/test_bank.py)

Unit tests for `bank.py` to ensure accurate functionality of the `value` function across various scenarios. Tests cover different greetings, including cases with leading spaces and variations in capitalization.

## 3. [Vanity Plates](Problem%20set%205%20Unit%20Tests/test_plates/)

### [plates.py](Problem%20set%205%20Unit%20Tests/test_plates/plates.py)

Implementation to validate vanity license plates according to specified rules. The `is_valid` function checks if a given license plate string meets the following requirements:
- Contains exactly 7 characters,
- Consists only of uppercase letters and digits,
- Does not start or end with a digit.

### [test_plates.py](Problem%20set%205%20Unit%20Tests/test_plates/test_plates.py)

Unit tests for `plates.py` to validate the `is_valid` function comprehensively. Tests include valid and invalid plates based on length, character composition, and position of digits.

## 4. [Fuel Gauge](Problem%20set%205%20Unit%20Tests/test_fuel/)

### [fuel.py](Problem%20set%205%20Unit%20Tests/test_fuel/fuel.py)

Implementation of functions related to converting fuel gauge readings and providing status. Includes:
- `convert`: Converts a string in the format "X/Y" to a percentage rounded to the nearest integer between 0 and 100. Raises errors for invalid formats or divisions by zero.
- `gauge`: Returns a status string based on an integer input:
  - "E" if the integer is less than or equal to 1,
  - "F" if the integer is greater than or equal to 99,
  - "Z%" otherwise, where Z is the integer.

### [test_fuel.py](Problem%20set%205%20Unit%20Tests/test_fuel/test_fuel.py)

Unit tests for `fuel.py` to validate the `convert` and `gauge` functions comprehensively. Tests include valid conversions, edge cases for division errors, and checks for correct status string outputs based on integer inputs.






# Problem Set 6
## 1. [Lines of Code](Problem%20set%206%20File%20Input%20Output/lines/)

### [lines.py](Problem%20set%206%20File%20Input%20Output/lines/lines.py)

**Description:** Measures the number of lines of code (LOC) in a Python file, excluding comments and blank lines.
**File:** `lines.py`

This program calculates and outputs the total lines of code in a specified Python file, excluding comments and blank lines. It opens the specified file using `open()`, and applies string manipulation methods to filter out ***comments*** and ***blank lines*** before counting the remaining lines of code. Here, we ignore ***docstring*** as a comments.

## 2. [Pizza](Problem%20set%206%20File%20Input%20Output/pizza/)

### [pizza.py](Problem%20set%206%20File%20Input%20Output/pizza/pizza.py)

**Description:** Generates an ASCII art table from a CSV file containing pizza data using the tabulate module.
**Files:**
  `pizza.py`
  `sicilian.csv`
  `regular.csv`

This program reads pizza data from two CSV files (`sicilian.csv` and `regular.csv`) using `csv.DictReader`, processes the data to generate an ASCII art table using the `tabulate` module, and prints the formatted table to the console in GRID format.

## 3. [Scourgify](Problem%20set%206%20File%20Input%20Output/scourgify/)

### [scourgify.py](Problem%20set%206%20File%20Input%20Output/scourgify/scourgify.py)

**Description:** Cleans and restructures CSV data containing student names and houses.
**Files:**
  `scourgify.py`
  `before.csv`
  `before.csv`

This program reads student data from `before.csv`, which contains combined names and house information, splits each full name into first and last names, then writes the cleaned data to a new CSV file (`after.csv`) using `csv.DictWriter`.

## 4. [Shirt](Problem%20set%206%20File%20Input%20Output/shirt/)

### [shirt.py](Problem%20set%206%20File%20Input%20Output/shirt/shirt.py)

**Files:**
  `shirt.py`, `before1.jpg`, `before2.jpg`, `before3.jpg`, `shirt.png`, `after1.jpg`

This program overlays a shirt image (`shirt.png`) onto three different photos (`before1.jpg`, `before2.jpg`, `before3.jpg`). It resizes and crops each photo to fit the dimensions of the shirt image using the `PIL` (Python Imaging Library) i.e (pillow packages), then saves the resulting images as new files (`after1.jpg`, `after2.jpg`, `after3.jpg`). Two modules are used from PIL packages: 1. Image and ImageOps







# Problem Set 7

## 1. [NUMB3RS](Problem%20set%207%20Regular%20Expressions/numb3rs/)

### [numb3rs.py](Problem%20set%207%20Regular%20Expressions/numb3rs//numb3rs.py)

**Description:** This program implements a function `validate` that checks if a given input string represents a valid IPv4 address.

**Function:** `validate(ip)`

Returns `True` if the input is a valid IPv4 address (in dot-decimal notation), otherwise `False`.

### [test_numb3rs.py](Problem%20set%207%20Regular%20Expressions/numb3rs/test_numb3rs.py)

**Description:** This file contains test functions to thoroughly test the `validate` function in `numb3rs.py`. Functions prefixed with `test_` validate different aspects of the `validate` function's behavior using pytest.

## 2. [response](Problem%20set%207%20Regular%20Expressions/response/)

### [response.py](Problem%20set%207%20Regular%20Expressions/response/response.py)

**Description:** This program prompts the user for an email address and validates whether it is syntactically valid according to a standard email format.

**Function:** `main()`

- Prompts the user for an email address input.
- Validates the email address using a specific library.
- Prints "Valid" if the email address is syntactically valid; otherwise, prints "Invalid".

## 3. [um](Problem%20set%207%20Regular%20Expressions/um/)

### [um.py](Problem%20set%207%20Regular%20Expressions/um/um.py)

**Description:** This program counts the occurrences of the word "um" (case-insensitive) as a standalone word in a given line of text.

**Function:** `count(s)`

- `s`: Input string in which to count occurrences of "um".

Returns an integer representing the count of "um" as a standalone word in the input text.

### [test_um.py](Problem%20set%207%20Regular%20Expressions/um/test_um.py)

**Description:** This file contains test functions to thoroughly test the `count` function in `um.py`. Functions prefixed with `test_` validate different scenarios and edge cases for the `count` function using pytest.

## 4. [watch](Problem%20set%207%20Regular%20Expressions/watch/)

### [watch.py](Problem%20set%207%20Regular%20Expressions/watch/watch.py)

**Description:** This program extracts a YouTube video ID from a given HTML string that contains an iframe element with a YouTube embed URL as its `src` attribute. It then converts this URL to the shorter youtu.be format.

**Function:** `parse(s)`

- `s`: Input HTML string containing an iframe element with a YouTube embed URL in `src` attribute.

Returns the youtu.be equivalent URL extracted from the input HTML string, or `None` if no valid URL is found.

## 5. [working](Problem%20set%207%20Regular%20Expressions/working/)

### [working.py](Problem%20set%207%20Regular%20Expressions/working/working.py)

**Description:** This program converts a time range in 12-hour AM/PM format to 24-hour military time format. It validates the input format and raises a `ValueError` for invalid formats or times.

**Function:** `convert(s)`

- `s`: Input string representing a time range in 12-hour AM/PM format.

Returns the corresponding time range in 24-hour format (e.g., "9:00 AM to 5:00 PM" -> "09:00 to 17:00").

### [test_working.py](Problem%20set%207%20Regular%20Expressions/working/test_working.py)

**Description:** This file contains test functions to thoroughly test the `convert` function in `working.py`. Functions prefixed with `test_` validate different scenarios and edge cases for the `convert` function using pytest.


## Feel free to explore each problem set, run the programs, and modify them as needed!

