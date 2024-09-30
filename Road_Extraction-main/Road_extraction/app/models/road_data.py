from sqlalchemy import Column, Integer, String, Date
from app.utils.database_utils import db

class RoadData(db.Model):  # Inherit from db.Model
    __tablename__ = 'road_data'
    
    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    region = Column(String, nullable=False)
    sensor = Column(String, nullable=False)

    def __repr__(self):
        return f'<RoadData {self.id}: {self.region} - {self.date}>'  # Optional for debugging

    def as_dict(self):
        """Convert the RoadData object into a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'image_path': self.image_path,
            'date': self.date.isoformat() if self.date else None,
            'region': self.region,
            'sensor': self.sensor
        }

class RoadChange(db.Model):  # Inherit from db.Model
    __tablename__ = 'road_change'
    
    id = Column(Integer, primary_key=True, index=True)
    change_image_path = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    region = Column(String, nullable=False)
    detected_on = Column(Date, nullable=False)

    def __repr__(self):
        return f'<RoadChange {self.id}: {self.region} - {self.detected_on}>'  # Optional for debugging

    def as_dict(self):
        """Convert the RoadChange object into a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'change_image_path': self.change_image_path,
            'date': self.date.isoformat() if self.date else None,
            'region': self.region,
            'detected_on': self.detected_on.isoformat() if self.detected_on else None
        }


