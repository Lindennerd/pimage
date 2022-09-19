from flask import Flask, Blueprint
from flask_restx.api import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from api.controllers import image

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

api = Api(app, 
    title='An Image processing Python API', 
    version='1.0', 
    description='This api primarily receives an image and then do stuff with it', 
    prefix='/api')
api.add_namespace(image.api, path='/image')
