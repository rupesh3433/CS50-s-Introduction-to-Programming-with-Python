import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError()

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_minute = start_minute or "00"
    end_minute = end_minute or "00"

    start_time = convert_to_24_hour(start_hour, start_minute, start_period)
    end_time = convert_to_24_hour(end_hour, end_minute, end_period)

    return f"{start_time} to {end_time}"

# Convert 12-hour format to 24-hour format
def convert_to_24_hour(hour, minute, period):
    hour = int(hour) % 12
    if period == "PM":
        hour += 12
    return f"{hour:02}:{minute}"


if __name__ == "__main__":
    main()
