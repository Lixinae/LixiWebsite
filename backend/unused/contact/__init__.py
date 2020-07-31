from flask import Blueprint

contact_bp = Blueprint('contact_bp', __name__,
                       static_folder='static',
                       template_folder='templates')

from backend.contact import routes
