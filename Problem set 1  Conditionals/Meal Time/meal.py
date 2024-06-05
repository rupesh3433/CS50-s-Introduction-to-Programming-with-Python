
def main():
    time = input("What time is it? ").strip()
    hours = convert(time)
    if hours >= 7 and hours <=8:
        print("breakfast time")
    if hours >= 12 and hours <=13:
        print("lunch time")
    if hours >= 18 and hours <=19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hours = float(hour) + float(minute)/60.0
    return hours


if __name__ == "__main__":
    main()
