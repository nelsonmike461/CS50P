def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shortened = []
    for char in word:
        if char.casefold() not in vowels:
            shortened.append(char)
    output = str("".join(shortened))
    return output


if __name__ == "__main__":
    main()
