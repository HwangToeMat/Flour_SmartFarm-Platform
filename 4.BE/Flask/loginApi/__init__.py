from flask import Blueprint

api_l = Blueprint('api_l', __name__)

from . import loginApi
