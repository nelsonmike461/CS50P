import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define a regular expression for a valid IPv4 address
    regex = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    # Try to match the regular expression with the input
    match = re.search(r"^" + regex + r"\." + regex + r"\." + regex + r"\." + regex + "$", ip)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
