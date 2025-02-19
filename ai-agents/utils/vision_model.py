import pytesseract
import cv2
import numpy as np

def extract_text_from_image(image):
    """Extract text from an uploaded image using OCR."""
    image = np.array(image)
    text = pytesseract.image_to_string(image)
    return text.strip()

