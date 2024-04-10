def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
    if 6 >= len(p) >= 2 and p[0:2].isalpha() and p.isalnum():
        for char in p:
            if char.isdigit():
                index = p.index(char)
                if p[index:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False
        return True


main()
