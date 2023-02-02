import pytesseract
import argparse
import cv2

ap = argparse.ArgumentParser()
'''ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")'''
ap.add_argument("-d", "--digits", type=int, default=1,
                help="whether or not *digits only* OCR will be performed")
args = vars(ap.parse_args())

image = cv2.imread('test_image.png')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

if args["digits"] > 0:
    options = "outputbase digits"

text = pytesseract.image_to_string(rgb)
print(text)