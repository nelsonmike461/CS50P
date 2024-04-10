import sys

def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        # Check if the file is a Python file
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            # Call the function to count lines
            print(count_lines(sys.argv[1]))

def count_lines(file):
    try:
        counter = 0
        # Open the file
        with open(file, "r") as f:
            for line in f:
                # Ignore lines that are comments or empty
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    counter = counter + 1
            return counter
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
