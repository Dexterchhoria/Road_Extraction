from sqlalchemy import Column, Integer, String, Date
from app.utils.database_utils import Base

class RoadData(Base):
    __tablename__ = 'road_data'
    
    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    region = Column(String, nullable=False)
    sensor = Column(String, nullable=False)

class RoadChange(Base):
    __tablename__ = 'road_changes'
    
    id = Column(Integer, primary_key=True, index=True)
    change_image_path = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    region = Column(String, nullable=False)
    detected_on = Column(Date, nullable=False)


