try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

#print(pytesseract.image_to_string(Image.open('test1.png')))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

#print(pytesseract.image_to_string(Image.open('1.jpg')))
print(pytesseract.image_to_string(Image.open('456.png')))

