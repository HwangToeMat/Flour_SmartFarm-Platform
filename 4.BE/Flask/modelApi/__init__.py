from flask import Blueprint

api_m = Blueprint('api_m', __name__)

from . import modelApi
