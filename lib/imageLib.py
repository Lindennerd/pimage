from PIL import Image, ImageFont, ImageDraw
import urllib.request as request
import string
import random
import base64
import os

dir = os.path.join(os.path.dirname(__file__), '../assets')

def random_name():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))

def get_base64_str(image):
    with open(image, 'rb') as file:
        str64 = base64.b64encode(file.read())
    
    print(str64)
    return str64

def pasteTextToImage(image_url, text):
    temp_name = os.path.join(dir, random_name() + '.jpg')
    request.urlretrieve(image_url, temp_name)

    image = Image.open(temp_name)
    font = ImageFont.truetype(os.path.join(dir,'segoeui.ttf'), 32)

    editable = ImageDraw.Draw(image)
    editable.text((10,90), text, (0, 0, 0), font=font)

    image.save(temp_name)

    return get_base64_str(temp_name)