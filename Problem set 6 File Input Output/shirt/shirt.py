import os
import sys
from PIL import Image, ImageOps

def main():
    # Validate command-line arguments and get input and output image paths
    input_image_path, output_image_path = check_valid_command_line_arguments()

    # Process the input image and overlay the shirt image
    overlap_shirt_image_to_body(input_image_path, output_image_path)

def overlap_shirt_image_to_body(input_image_path, output_image_path):
    # Open the input image and shirt image
    input_image_object = Image.open(input_image_path)
    shirt_image_object = Image.open("shirt.png")

    # Resize and crop the input image to match the size of the shirt image
    input_image_resized = ImageOps.fit(input_image_object, shirt_image_object.size)

    # Overlay the shirt image onto the resized input image
    input_image_resized.paste(shirt_image_object, shirt_image_object)

    # Save the resulting image to the output path
    input_image_resized.save(output_image_path)

def check_valid_command_line_arguments():
    # Check for the correct number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Get input and output image paths from command-line arguments
    img1 = sys.argv[1].lower().strip()
    img2 = sys.argv[2].lower().strip()

    # Validate input and output image file extensions
    if not img1.endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    if not img2.endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    # Ensure input and output files have the same extension
    if img1[img1.rfind("."):] != img2[img2.rfind("."):]:
        sys.exit("Input and output have different extensions")

    # Check if the input file exists
    if not os.path.exists(img1):
        sys.exit("Input does not exist")

    return [img1, img2]

if __name__ == "__main__":
    main()
