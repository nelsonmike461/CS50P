def main():
    # Prompt the user for a time
    time_str = input("Enter a time (24-hour format): ")
    # Convert the time to a float
    time_float = convert(time_str)
    # Determine the meal time
    if 7 <= time_float < 9:
        print("breakfast time")
    elif 12 <= time_float < 14:
        print("lunch time")
    elif 18 <= time_float < 21:
        print("dinner time")

def convert(time_str):
    # Split the time into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    # Convert the time to a float
    time_float = hours + minutes / 60
    return time_float

if __name__ == "__main__":
    main()
