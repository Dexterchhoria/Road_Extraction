from flask import Flask
from app.api.alert import alert_blueprint
from app.api.road_data import road_data_blueprint
from app.api.image_processing import image_processing_blueprint
from app.utils.database_utils import init_db

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(alert_blueprint, url_prefix='/alert')
    app.register_blueprint(road_data_blueprint, url_prefix='/road_data')
    app.register_blueprint(image_processing_blueprint, url_prefix='/image_processing')

    # Initialize the database
    init_db(app)
    
    return app

