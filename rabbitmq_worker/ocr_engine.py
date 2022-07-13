import pytesseract as tes
from io import BytesIO
import base64
import os
from PIL import Image
import time
tes.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

def b64string_to_text(_id, image_info):
    image_bytes = BytesIO(base64.b64decode(image_info))
    image = Image.open(image_bytes)
    image.save("temp.png", "PNG")
    image = Image.open("temp.png")
    data = tes.image_to_string(image)
    os.remove("temp.png")
    return data
    
