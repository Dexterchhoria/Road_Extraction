from sqlalchemy.orm import Session
from app.models.road_data import RoadData, RoadChange
from app.utils.database_utils import get_db_session
import os

# Service to handle road data operations
class RoadDataService:
    
    def __init__(self):
        self.db: Session = get_db_session()
    
    def save_road_data(self, image_path: str, metadata: dict):
        """
        Saves the road extraction data into the database.
        
        Args:
            image_path (str): Path to the saved road extraction image.
            metadata (dict): Metadata related to the image (e.g., date, region).
        """
        new_road_data = RoadData(
            image_path=image_path,
            date=metadata['date'],
            region=metadata['region'],
            sensor=metadata['sensor']
        )
        
        self.db.add(new_road_data)
        self.db.commit()
        print(f"Road data saved: {image_path}")
    
    def save_road_changes(self, change_image_path: str, metadata: dict):
        """
        Saves the detected road changes into the database.
        
        Args:
            change_image_path (str): Path to the saved road changes image.
            metadata (dict): Metadata related to the road changes (e.g., date, region).
        """
        new_road_change = RoadChange(
            change_image_path=change_image_path,
            date=metadata['date'],
            region=metadata['region'],
            detected_on=metadata['detected_on']
        )
        
        self.db.add(new_road_change)
        self.db.commit()
        print(f"Road changes saved: {change_image_path}")
    
    def get_road_data(self, region: str, date: str):
        """
        Retrieves road data from the database based on region and date.
        
        Args:
            region (str): Region of the road data.
            date (str): Date of the road extraction.
        
        Returns:
            RoadData: The road data from the database.
        """
        return self.db.query(RoadData).filter_by(region=region, date=date).first()
    
    def get_road_changes(self, region: str, date: str):
        """
        Retrieves road changes from the database based on region and date.
        
        Args:
            region (str): Region of the road changes.
            date (str): Date of the road changes detection.
        
        Returns:
            RoadChange: The road change data from the database.
        """
        return self.db.query(RoadChange).filter_by(region=region, date=date).first()
