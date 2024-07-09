
from PIL import Image
import sys
import numpy as np

def convert():
    filename = sys.argv[1]
    asciiRep = ""
    targetWidth = 80
    with Image.open(filename) as img:
        aspectRatio = img.height / img.width
        targetHeight = int(aspectRatio*targetWidth*0.55)
        img = img.resize((targetWidth, targetHeight))
    
    asciiMap = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '&', '8', 'B', 'W', '#', '%']
    pixels = list(img.getdata())
    for i in range(len(pixels)):
        if (i % img.width == 0):
            asciiRep += "\n"
        avg = np.mean(pixels[i])
        asciiRep += asciiMap[int(avg) * len(asciiMap) // 256]
    print(asciiRep)

if __name__ == "__main__":
    convert()