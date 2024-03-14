from PIL import Image
import pytesseract
x='C:\Users\rishi\Desktop\OPENCV\text.png'
def detect_text(x):
    # Open image
    img = Image.open(x)
    # Use pytesseract to detect text
    text = pytesseract.image_to_string(img)
    
    return text

# Test the function
print(detect_text(x))
