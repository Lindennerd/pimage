from flask_restx import Resource, Namespace, fields
from flask import request
from lib import imageLib

api = Namespace('Image processing API')
model = api.model('ImageModel', {
    'imageUrl': fields.String,
    'text': fields.String
})

@api.route('/')
class ImageController(Resource):
    @api.response(200, "returns the image with the defined text")
    def get(self):
        return 'teste', 200