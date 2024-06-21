import os
import sys

def main():
    # Validate the command line arguments and get the file name
    file = check_valid_command_line_arguments()
    # Count the number of lines of code in the file
    line_count = count_no_of_lines(file)
    # Print the number of lines of code
    print(line_count)


def check_valid_command_line_arguments():
    # Check if there are exactly one or more than two command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file = sys.argv[1]
    # Check if the specified file exists or not using the "os" module
    if not os.path.exists(file):
        sys.exit("File does not exist")
    # Check if the file name is long enough to have a valid extension and check if it has .py extension
    if len(file) < 4 or not file.endswith('.py'):
        sys.exit("Not a Python file")

    return file

def count_no_of_lines(file):
    with open(file) as python_file:
        inside_docstring = False
        count_line = 0
        for row in python_file:
            row = row.strip()
            # Skip empty lines and Skip single-line comments
            if not row or row.startswith("#"):
                continue

            # Handle docstrings
            if row.startswith(('"""', "'''")):
                inside_docstring = not inside_docstring
                count_line += 1
                continue
            if inside_docstring:
                count_line += 1
                continue

            count_line += 1

    return count_line



if __name__ == "__main__":
    main()
