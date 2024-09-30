from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Import all models so they are registered with SQLAlchemy
from app.models.road_data import RoadData, RoadChange
from app.models.image_metadata import ImageMetadata
from app.models.alert import Alert
from app.models.satellite_images import SatelliteImage  # <-- Import the new model

def init_db(app):
    """Initializes the database with the provided Flask app."""
    db.init_app(app)
    with app.app_context():
        db.create_all()  # This will create all tables if they don't exist
