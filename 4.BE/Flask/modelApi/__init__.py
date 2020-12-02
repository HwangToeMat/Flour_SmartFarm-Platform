from flask import Blueprint

api_model = Blueprint('api_model', __name__)

from . import modelApi
