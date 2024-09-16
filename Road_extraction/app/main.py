# main.py

from flask import Flask
from app.config import email_config
from app.api import alert, gateway, image_processing, road_data
from app.services import alert_service, image_processing_service, road_data_service

def create_app():
    """
    Create and configure an instance of the Flask application.
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_mapping(
        SMTP_SERVER=email_config.SMTP_SERVER,
        SMTP_PORT=email_config.SMTP_PORT,
        EMAIL_USER=email_config.EMAIL_USER,
        EMAIL_PASSWORD=email_config.EMAIL_PASSWORD,
    )
    
    # Register blueprints
    app.register_blueprint(alert.bp)
    app.register_blueprint(gateway.bp)
    app.register_blueprint(image_processing.bp)
    app.register_blueprint(road_data.bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)  # Use debug=True for development; set to False in production
