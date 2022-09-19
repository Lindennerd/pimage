from PIL import Image, ImageFont, ImageDraw
import urllib.request as request
import string
import random
import base64
import os

assets_dir = os.path.join(os.path.dirname(__file__), '../assets')
temp_dir = os.path.join(os.path.dirname(__file__), '../temp')

def random_name():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))

def get_base64_str(image):
    with open(image, 'rb') as file:
        str64 = base64.b64encode(file.read())
    
    print(str64)
    return str64

def delete_temp_image(image):
    os.remove(image)

def pasteTextToImage(image_url, text):
    temp_name = os.path.join(temp_dir, random_name() + '.jpg')
    request.urlretrieve(image_url, temp_name)

    image = Image.open(temp_name)
    font = ImageFont.truetype(os.path.join(assets_dir,'segoeui.ttf'), 32)

    editable = ImageDraw.Draw(image)
    editable.text((10,90), text, (0, 0, 0), font=font)

    image.save(temp_name)

    strb64 = get_base64_str(temp_name)
    delete_temp_image(temp_name)
    return strb64