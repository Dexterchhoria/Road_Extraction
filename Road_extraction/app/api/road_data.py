from flask import Blueprint, request, jsonify
from app.models.road_data import RoadData, RoadChange
from app.utils.database_utils import db
from datetime import date

road_data_blueprint = Blueprint('road_data', __name__)

@road_data_blueprint.route('/<string:region>', methods=['GET'])
def get_road_data(region):
    road_data = RoadData.query.filter_by(region=region).all()

    if not road_data:
        return jsonify({'error': 'No road data found for this region'}), 404

    return jsonify([data.as_dict() for data in road_data])

@road_data_blueprint.route('/road_changes/<string:region>', methods=['GET'])
def get_road_changes(region):
    road_changes = RoadChange.query.filter_by(region=region).all()

    if not road_changes:
        return jsonify({'error': 'No road changes found for this region'}), 404

    return jsonify([change.as_dict() for change in road_changes])

@road_data_blueprint.route('/', methods=['POST'])
def add_road_data():
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


@road_data_blueprint.route('/road_change', methods=['POST'])
def add_road_change():
    data = request.get_json()
    road_change = RoadChange(
        change_image_path=data.get('change_image_path'),
        region=data.get('region'),
        date=date.today(),
        detected_on=date.today()
    )
    db.session.add(road_change)
    db.session.commit()

    return jsonify({'message': 'Road change added successfully'})
