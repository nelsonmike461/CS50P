def main():
    num = input("Fraction: ")
    percentage = convert(num)
    print(gauge(percentage))


def convert(num):
    while True:
        index = num.find("/")
        try:
            x = int(num[:index])
            y = int(num[index + 1:])
            fraction = x / y
            if x > y:
                num = input("Fraction: ")
                continue
            else:
                percentage = int(fraction * 100)
                return percentage
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return(str(percentage) + "%")


if __name__ == "__main__":
    main()
