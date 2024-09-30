from flask import Blueprint, request, jsonify
from app.models.road_data import RoadData, RoadChange
from app.models.satellite_images import SatelliteImage
from app.services.alert_service import send_alert
from app.utils.database_utils import db
from datetime import date

road_data_blueprint = Blueprint('road_data', __name__)

# Get road data for a specific region
@road_data_blueprint.route('/<string:region>', methods=['GET'])
def get_road_data(region):
    try:
        road_data = RoadData.query.filter_by(region=region).all()

        if not road_data:
            return jsonify({'error': 'No road data found for this region'}), 404

        return jsonify([data.as_dict() for data in road_data])
    except Exception as e:
        print(f"Error fetching road data: {e}")  # Log the error to the console
        return jsonify({'error': 'Internal Server Error'}), 500


# Get road changes for a specific region
@road_data_blueprint.route('/road_changes/<string:region>', methods=['GET'])
def get_road_changes(region):
    try:
        road_changes = RoadChange.query.filter_by(region=region).all()

        if not road_changes:
            return jsonify({'error': 'No road changes found for this region'}), 404

        return jsonify([change.as_dict() for change in road_changes])
    except Exception as e:
        print(f"Error fetching road changes: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


# Add road data
@road_data_blueprint.route('/', methods=['POST'])
def add_road_data():
    try:
        data = request.get_json()
        road_data = RoadData(
            image_path=data.get('image_path'),
            region=data.get('region'),
            sensor=data.get('sensor'),
            date=date.today()
        )
        db.session.add(road_data)
        db.session.commit()

        return jsonify({'message': 'Road data added successfully'})
    except Exception as e:
        print(f"Error adding road data: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


# Add road change
@road_data_blueprint.route('/road_change', methods=['POST'])
def add_road_change():
    try:
        data = request.get_json()
        road_change = RoadChange(
            change_image_path=data.get('change_image_path'),
            region=data.get('region'),
            date=date.today(),
            detected_on=date.today()
        )
        db.session.add(road_change)
        db.session.commit()

        # Automatically send an alert after successfully adding the road change
        alert_message = f"Road changes detected in region: {road_change.region} on {road_change.date}."
        
        # Use the hardcoded email address
        email = "22mc3038@rgipt.ac.in"

        # Send the alert email
        try:
            send_alert(email, alert_message)  # Ensure this is called
            print("Alert sent successfully.")
            return jsonify({'message': 'Road change added successfully, alert sent!'})
        except Exception as e:
            print(f"Error sending alert: {e}")
            return jsonify({'message': 'Road change added successfully, but alert failed to send.'})

    except Exception as e:
        print(f"Error adding road change: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


# Fetch all satellite images
@road_data_blueprint.route('/satellite_images', methods=['GET'])
def get_satellite_images():
    try:
        satellite_images = SatelliteImage.query.all()

        if not satellite_images:
            return jsonify({'error': 'No satellite images found'}), 404

        return jsonify([{'file_name': image.file_name, 'image_date': image.image_date} for image in satellite_images])
    except Exception as e:
        print(f"Error fetching satellite images: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


# Add satellite image metadata
@road_data_blueprint.route('/satellite_images', methods=['POST'])
def add_satellite_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        file = request.files['image']
        image_date = request.form.get('image_date')

        if not image_date:
            return jsonify({'error': 'Image date is required'}), 400

        new_image = SatelliteImage(
            file_name=file.filename,
            image_date=image_date,
            file_data=file.read()
        )

        db.session.add(new_image)
        db.session.commit()

        return jsonify({'message': 'Satellite image added successfully'})
    except Exception as e:
        print(f"Error adding satellite image: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
