import csv
import sys
from tabulate import tabulate

def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        # Check if the file is a CSV file
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            # Call the function to tabulate the CSV file
            print(tabulize(sys.argv[1]))

def tabulize(file):
    try:
        # Open the file
        with open(file) as f:
            # Read the file using csv.reader
            reader = csv.reader(f)
            # Tabulate the contents of the file
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
