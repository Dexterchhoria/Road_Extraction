from flask import Blueprint, jsonify, request
from app.services.image_processing_service import extract_roads

image_processing_bp = Blueprint('image_processing', __name__)

@image_processing_bp.route('/process-image', methods=['POST'])
def process_image():
    image_path = request.json.get('image_path')
    road_shapefile = extract_roads(image_path)
    return jsonify({"message": "Roads extracted", "shapefile": road_shapefile})
