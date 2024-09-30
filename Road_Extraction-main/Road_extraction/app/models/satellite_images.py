# app/models/satellite_images.py
from app.utils.database_utils import db
from sqlalchemy import LargeBinary, Date, String, Integer

class SatelliteImage(db.Model):
    __tablename__ = 'satellite_images'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    image_date = db.Column(db.Date, nullable=False)
    file_data = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, file_name, image_date, file_data):
        self.file_name = file_name
        self.image_date = image_date
        self.file_data = file_data

    def as_dict(self):
        return {
            'id': self.id,
            'file_name': self.file_name,
            'image_date': self.image_date,
            'file_size': len(self.file_data)
        }
