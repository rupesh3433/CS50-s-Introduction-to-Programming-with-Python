
#Global list that store months
valid_months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

#Main Function
def main():
    while True:
        us_format = input("Date: ").strip()
        if valid_us_format(us_format):
            standard_format = convert_us_to_standard_format(us_format)
            print(standard_format)
            break
        else:
            continue


#Functions for validation of US Format
def valid_us_format(us_format):
    if slash_format(us_format) or space_comma_format(us_format):
        return True
    return False

def slash_format(us_format):
    try:
        months, day, year = us_format.split("/")
        months = int(months)
        day = int(day)
        year = int(year)
        if (months > 11) or (day > 31):
            return False
        else:
            return True
    except ValueError:
        return False

def space_comma_format(us_format):
    try:
        months, day, year = us_format.split(" ")
        day = int(day[:len(day)-1])
        year = int(year)
        if (not months in valid_months) or (day > 31):
            return False
        else:
            return True
    except ValueError:
        return False


#functions for conversion from us format to standard format
def convert_us_to_standard_format(us_format):
    if slash_format(us_format):
        standard_format = convert_slash_to_standard(us_format)
    elif space_comma_format(us_format):
        standard_format = convert_space_comma_to_standard(us_format)
    return standard_format

def convert_slash_to_standard(us_format):
    months, day, year = us_format.split("/")
    if len(months) != 2:
        months = "0" + months
    if len(day) != 2:
        day = "0" + day
    standard_format = year + "-" + months + "-" + day
    return standard_format

def convert_space_comma_to_standard(us_format):
    months, day, year = us_format.split(" ")
    day = day[:len(day)-1]
    months_in_number = valid_months.index(months) + 1
    months_in_string = str(months_in_number)
    if len(months_in_string) != 2:
        months_in_string = "0" + months_in_string
    if len(day) != 2:
        day = "0" + day
    standard_format = year + "-" + months_in_string + "-" + day
    return standard_format


main()
