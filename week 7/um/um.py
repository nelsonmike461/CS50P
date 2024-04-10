import re


def main():
    print(count(input("Text: ")))


def count(m):
    regex = r"\bum\b"
    match = re.findall(regex, m, re.IGNORECASE)
    return(len(match))


if __name__ == "__main__":
    main()
