from flask import Blueprint
from app.api.image_metadata import image_metadata_bp
from app.api.alert import alert_blueprint
from app.api.road_data import road_data_blueprint
from app.api.image_processing import image_processing_blueprint
from app.api.gateway import gateway_bp  # Import the gateway blueprint correctly

api_bp = Blueprint('api', __name__)

# Register all blueprints with their respective URL prefixes
api_bp.register_blueprint(image_metadata_bp, url_prefix='/image_metadata')
api_bp.register_blueprint(alert_blueprint, url_prefix='/alert')
api_bp.register_blueprint(road_data_blueprint, url_prefix='/road_data')
api_bp.register_blueprint(image_processing_blueprint, url_prefix='/image_processing')
api_bp.register_blueprint(gateway_bp, url_prefix='/gateway')




