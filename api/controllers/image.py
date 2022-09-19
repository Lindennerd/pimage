from flask_restx import Resource, Namespace, fields
from flask import request
from lib import imageLib

api = Namespace('Image processing API')
model = api.model('ImageModel', {
    'imageUrl': fields.String,
    'text': fields.String
})

@api.route('/pasteTextOnImage')
class ImageController(Resource):

    @api.response(200, "Returns the image with the defined text")
    @api.response(400, "Returns Bad Request if any parameter is blank or null")
    @api.param('imageUrl', 'Url of the image to paste the text on')
    @api.param('text', 'The text to be pasted on the image')
    def get(self):
        imageUrl = request.args.get('imageUrl');
        text = request.args.get('text');

        if imageUrl is None or imageUrl == '':
            return 'You must provide an image url', 400

        if text is None:
            return 'You must provide a text', 400

        return {'image': 'data:image/jpg;base64,' + imageLib.pasteTextToImage(imageUrl, text)}, 200