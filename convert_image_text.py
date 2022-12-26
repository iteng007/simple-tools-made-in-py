import pytesseract
from PIL import Image
import sys
if (len(sys.argv)!=2):
    print("wrong usage need image's name")
    exit(1)

image = Image.open(sys.argv[1])

text = pytesseract.image_to_string(image,lang='chi_sim')

with open("output.txt","a") as f:
    f.write(text)
