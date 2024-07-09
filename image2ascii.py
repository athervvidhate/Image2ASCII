
from PIL import Image
import sys
import numpy as np

def convert():

    filename = sys.argv[1]
    asciiRep = ""

    # Default width of 80 for command line interfaces, can be edited to change how the image looks.
    targetWidth = 80 

    # Resizes the image to be smaller, so that the function has less data to go through
    with Image.open(filename) as img:
        aspectRatio = img.height / img.width
        targetHeight = int(aspectRatio*targetWidth*0.55)
        img = img.resize((targetWidth, targetHeight))
    
    # Contains all the different brightness levels for each pixel
    asciiMap = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '&', '8', 'B', 'W', '#', '%']

    # Creates a list of all of the RGB values for each pixel in the image
    pixels = list(img.getdata())

    # Creates the ASCII art
    for i in range(len(pixels)):
        if (i % img.width == 0):
            asciiRep += "\n"
        
        # Takes the average of the RGB values to get a brightness value
        avg = np.mean(pixels[i])

        asciiRep += asciiMap[int(avg) * len(asciiMap) // 256]
    print(asciiRep)

if __name__ == "__main__":
    convert()