#!/usr/bin/python3

print("If you don't have tessaract-ocr and libtesseract-dev installed, please install by running below command.")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("sudo apt-get install tesseract-ocr && sudo apt-get install libtesseract-dev")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
from PIL import Image
from pytesseract import pytesseract

# Defining paths to tesseract
# and the image we would be using

path_to_tesseract = r"/usr/bin/tesseract"
image_path=input("Please enter the full path to the PNG format image: ")


#print(image_path)

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)

# Displaying the extracted text
print("\nThe extracted text is given below:\n")
print(text[:-1])
