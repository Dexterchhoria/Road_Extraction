from flask import Blueprint, jsonify, request
from app.services.alert_service import generate_alert

alert_bp = Blueprint('alert', __name__)

@alert_bp.route('/alert', methods=['POST'])
def alert_new_road():
    area_id = request.json.get('area_id')
    result = generate_alert(area_id)
    return jsonify({"message": "Alert sent", "details": result})
