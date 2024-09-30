from flask import Blueprint, request, jsonify
from app.services.image_processing_service import process_images_and_detect_changes
from app.models.image_metadata import ImageMetadata
from app.models.satellite_images import SatelliteImage  # Import SatelliteImage model
from app.utils.database_utils import db
from datetime import datetime

image_processing_blueprint = Blueprint('image_processing', __name__)

@image_processing_blueprint.route('/process_images', methods=['POST'])
def process_images():
    # Assuming files are uploaded as part of the form data
    old_band_files = request.files.getlist('old_bands')
    new_band_files = request.files.getlist('new_bands')
    area_id = request.form.get('area_id')

    if not old_band_files or not new_band_files:
        return jsonify({'error': 'Missing image files'}), 400

    old_band_paths = []
    new_band_paths = []

    # Save the files to the disk
    for old_file, new_file in zip(old_band_files, new_band_files):
        old_path = f"data/{old_file.filename}"
        new_path = f"data/{new_file.filename}"
        
        old_file.save(old_path)
        new_file.save(new_path)
        
        old_band_paths.append(old_path)
        new_band_paths.append(new_path)

    # Process the images and detect changes
    change_image_path = process_images_and_detect_changes(old_band_paths, new_band_paths, area_id)
    
    if not change_image_path:
        return jsonify({'error': 'Failed to detect road changes'}), 500

    # Save metadata to the database
    metadata = ImageMetadata(
        source="Resourcesat", 
        capture_date=datetime.utcnow(), 
        band_paths=",".join(new_band_paths), 
        area_id=area_id
    )
    db.session.add(metadata)
    db.session.commit()

    return jsonify({'message': 'Road changes detected', 'change_image_path': change_image_path})

# New endpoint to process all satellite images from the database
@image_processing_blueprint.route('/process_all_satellite_images', methods=['POST'])
def process_all_satellite_images():
    # Fetch all satellite images from the database
    satellite_images = SatelliteImage.query.all()

    if not satellite_images:
        return jsonify({'error': 'No satellite images found to process'}), 404

    # Process each satellite image
    for image in satellite_images:
        # Assuming the processing function handles binary image data
        process_images_and_detect_changes([image.file_data], [image.file_data], area_id=None)

    return jsonify({'message': 'Processing of all satellite images completed.'})


