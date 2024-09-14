from flask import Blueprint, jsonify, request
from app.services.road_data_service import save_road_data

road_data_bp = Blueprint('road_data', __name__)

@road_data_bp.route('/road-data', methods=['POST'])
def store_road_data():
    road_shapefile = request.json.get('road_shapefile')
    save_road_data(road_shapefile)
    return jsonify({"message": "Road data saved to GIS database"})
