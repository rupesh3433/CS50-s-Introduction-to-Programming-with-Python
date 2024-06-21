import sys
import os
import csv
from tabulate import tabulate

def main():
    file = check_valid_arguments()
    make_ascii_grid_using_tabulate(file)


def make_ascii_grid_using_tabulate(file):
    header = header_of_table(file)
    table = lists_of_table(file, header)
    grid_table = tabulate(table, header, tablefmt = "grid")
    print(grid_table)


def lists_of_table(file, header):
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)
        list_of_lists = []
        for row in reader:
            list_of_row = [row[header[0]], row[header[1]], row[header[2]]]
            list_of_lists.append(list_of_row)
    return list_of_lists


def header_of_table(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
    return header


def check_valid_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    file = sys.argv[1]
    if not file.endswith(".csv"):
        sys.exit("Not a CSV file")
    if not os.path.exists(file):
        sys.exit("File does not exist")
    return file


if __name__ == "__main__":
    main()
