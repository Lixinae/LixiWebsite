from flask import Blueprint

contact_bp = Blueprint('contact_bp', __name__,
                       static_folder='static',
                       template_folder='templates')

from application.contact import routes
