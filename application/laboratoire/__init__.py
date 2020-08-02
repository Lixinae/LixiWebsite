from flask import Blueprint
import logging

logger = logging.getLogger('VahenWebsite.laboratoire')

laboratoire_bp = Blueprint('laboratoire_bp', __name__,
                           static_folder='static',
                           template_folder='templates',
                           url_prefix="/laboratoire")

from application.laboratoire import routes
