from lib import imageLib

if __name__ == '__main__':
    imageUrl = 'https://raw.githubusercontent.com/Lindennerd/olavo-tem-razao/master/public/olavo-post.jpg'
    text = 'dhasjkdhaskd'

    str = imageLib.pasteTextToImage(imageUrl, text)
    print(str)