from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgreSQL@localhost:5432/gisdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints
    from app.api.gateway import gateway_bp  # Ensure this matches the updated name
    from app.api import alert, image_processing, road_data, image_metadata  # Adjust as necessary

    # Register blueprints
    app.register_blueprint(gateway_bp, url_prefix='/gateway')
    # Register other blueprints...

    return app
