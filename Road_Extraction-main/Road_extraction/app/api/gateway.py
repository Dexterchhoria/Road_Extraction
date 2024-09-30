from flask import Blueprint
from app.api.alert import alert_blueprint
from app.api.road_data import road_data_blueprint
from app.api.image_processing import image_processing_blueprint

# Create the main gateway blueprint
gateway_bp = Blueprint('gateway', __name__)

@gateway_bp.route('/')
def index():
    return "Welcome to the Gateway!"

# Register sub-blueprints within the gateway blueprint
gateway_bp.register_blueprint(alert_blueprint, url_prefix='/alert')
gateway_bp.register_blueprint(road_data_blueprint, url_prefix='/road_data')
gateway_bp.register_blueprint(image_processing_blueprint, url_prefix='/image_processing')
