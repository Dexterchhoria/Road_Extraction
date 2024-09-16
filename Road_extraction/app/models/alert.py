from sqlalchemy import Column, Integer, String, Boolean
from app.utils.database_utils import Base

class Alert(Base):
    __tablename__ = 'alerts'
    
    id = Column(Integer, primary_key=True, index=True)
    area_id = Column(String, nullable=False)
    change_detected = Column(Boolean, nullable=False)
    message = Column(String, nullable=False)


