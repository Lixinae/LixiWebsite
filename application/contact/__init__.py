from flask import Blueprint

bp = Blueprint('contact', __name__)

from application.contact import routes
