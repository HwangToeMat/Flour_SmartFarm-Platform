from flask import Blueprint

api_t = Blueprint('api_t', __name__)

from . import tradeApi
