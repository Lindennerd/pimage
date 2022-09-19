from api import app
from os import environ
from lib import imageLib


if __name__ == '__main__':
    # imageUrl = 'https://raw.githubusercontent.com/Lindennerd/olavo-tem-razao/master/public/olavo-post.jpg'
    # text = 'dhasjkdhaskd'
    # str = imageLib.pasteTextToImage(imageUrl, text)
    # print(str)

    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(
        host=SERVER_HOST, 
        port=5500, 
        debug=(not environ.get('ENV') == 'production'), 
        threaded=True)
