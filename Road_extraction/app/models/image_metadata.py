from sqlalchemy import Column, Integer, String, DateTime
from app.utils.database_utils import Base

class ImageMetadata(Base):
    __tablename__ = 'image_metadata'
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)
    capture_date = Column(DateTime, nullable=False)
    band_paths = Column(String, nullable=False)
    area_id = Column(String, nullable=False)

