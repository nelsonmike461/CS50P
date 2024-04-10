from PIL import Image, ImageOps
import sys
import os

def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Check if the output file has a valid image extension
        format = [".jpg", ".jpeg", ".png"]
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])
        if outp[1].lower() not in format:
            sys.exit("Invalid output")
        # Check if the input and output files have the same extension
        elif inp[1].lower() != outp[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            edit_photo(sys.argv[1], sys.argv[2])

def edit_photo(input, output):
    try:
        # Open the overlay image
        shirt = Image.open("shirt.png")
        # Open the input image
        with Image.open(input) as input:
            # Resize the input image to match the size of the overlay image
            input_cropped = ImageOps.fit(input, shirt.size)
            # Overlay the images
            input_cropped.paste(shirt, mask = shirt)
            # Save the result
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

if __name__ == "__main__":
    main()
