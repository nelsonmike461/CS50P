import csv
import sys

def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Check if the file is a CSV file
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])

def clean(input, output):
    try:
        # Open the input file
        with open(input) as input:
            # Read the file using csv.DictReader
            reader = csv.DictReader(input)
            # Open the output file
            with open(output, "w") as output:
                # Define the headers for the output file
                header = ["first", "last", "house"]
                # Create a csv.DictWriter object
                writer = csv.DictWriter(output, fieldnames = header)
                writer.writeheader()
                # Iterate over the rows in the input file
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    # Write the cleaned data to the output file
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")

if __name__ == "__main__":
    main()
