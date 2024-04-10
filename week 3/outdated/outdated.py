months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            month_day, year = date.split(", ")
            month, day = month_day.split(" ")

            month = (months.index(month)) + 1
        if int(month) > 12 or int(day) > 31:
             raise ValueError
    except (ValueError, NameError, AttributeError, KeyError):
        pass
    else:
            print(f"{int(year)}-{int(month):02}-{int(day):02}")
            break




