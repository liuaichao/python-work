import pytesseract as pt
from PIL import Image
pt.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
img = Image.open(r'C:\Users\THINKPAD\Desktop\google.jpg')
text = pt.image_to_string(img)
print(text)