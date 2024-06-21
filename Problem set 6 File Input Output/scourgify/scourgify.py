import sys
import os
import csv

def main():
    file1, file2 = check_valid_arguments()
    list_after_spliting_name = lists_of_before_file(file1)
    create_after_csv_file(list_after_spliting_name, file2)


def lists_of_before_file(file1):
    with open(file1, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        list_of_dict = []
        for row in reader:
            lastname, firstname = row["name"].split(",")
            dict_of_row = {"first":firstname.strip(), "last":lastname.strip(), "house":row["house"]}
            list_of_dict.append(dict_of_row)
    return list_of_dict

def create_after_csv_file(list_after_spliting_name, file2):
    with open(file2, "w", newline='') as csv_file:
        header = ["first", "last", "house"]
        writer = csv.DictWriter(csv_file, fieldnames = header, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in list_after_spliting_name:
            writer.writerow({
                "first": row["first"],
                "last": row["last"],
                "house": f'"{row["house"]}"' if "," in row["house"] else row["house"]
            })

def check_valid_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    if not file1.endswith(".csv") and not file2.endswith(".csv"):
        sys.exit("Not a CSV file")
    if not os.path.exists(file1):
        sys.exit("File does not exist")
    return [file1, file2]


if __name__ == "__main__":
    main()
