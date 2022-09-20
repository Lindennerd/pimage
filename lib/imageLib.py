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
        str64 = base64.b64encode(file.read()).decode()
    
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
    init_x = 10
    init_y = 9
    for line in text_wrap(text, font, 700):
        editable.text((init_x, init_y), line, (0, 0, 0), font=font)
        init_y = init_y + 5

    image.save(temp_name)

    strb64 = get_base64_str(temp_name)
    delete_temp_image(temp_name)
    return str(strb64)

# REF https://itnext.io/how-to-wrap-text-on-image-using-python-8f569860f89e
def text_wrap(text, font, max_width):
        """Wrap text base on specified width. 
        This is to enable text of width more than the image width to be display
        nicely.
        @params:
            text: str
                text to wrap
            font: obj
                font of the text
            max_width: int
                width to split the text with
        @return
            lines: list[str]
                list of sub-strings
        """
        lines = []
        
        # If the text width is smaller than the image width, then no need to split
        # just add it to the line list and return
        if font.getsize(text)[0]  <= max_width:
            lines.append(text)
        else:
            #split the line by spaces to get words
            words = text.split(' ')
            i = 0
            # append every word to a line while its width is shorter than the image width
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                    line = line + words[i]+ " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines