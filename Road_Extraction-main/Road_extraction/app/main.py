from flask import Flask
from app.config import email_config
from app.api import api_bp  # Import the API blueprint which includes all routes
from app.utils.database_utils import db, init_db  # Import the SQLAlchemy instance and init function

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
        SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgreSQL@localhost:5432/gisdb',  # Update with your DB details
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # Initialize the database with the app
    init_db(app)

    # Register the API blueprint
    app.register_blueprint(api_bp, url_prefix='/api')  # Register the API blueprint with /api prefix

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
