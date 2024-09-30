from sqlalchemy import Column, Integer, String, Boolean
from app.utils.database_utils import db

class Alert(db.Model):  # Inherit from db.Model
    __tablename__ = 'alert'  # Specify the table name

    id = Column(Integer, primary_key=True, index=True)
    area_id = Column(String, nullable=False)
    change_detected = Column(Boolean, nullable=False)
    message = Column(String, nullable=False)

    def __repr__(self):
        return f'<Alert {self.id}: {self.message}>'  # Optional: Add a string representation for debugging



