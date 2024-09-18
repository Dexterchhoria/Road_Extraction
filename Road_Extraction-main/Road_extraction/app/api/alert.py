from flask import Blueprint, request, jsonify
from app.services.alert_service import send_alert
from app.models.alert import Alert
from app.models.road_data import RoadChange
from app.utils.database_utils import db

alert_blueprint = Blueprint('alert', __name__)

@alert_blueprint.route('/send_alert', methods=['POST'])
def send_change_alert():
    data = request.get_json()
    change_id = data.get('change_id')
    email = data.get('email')

    # Fetch the detected change from the database
    change = RoadChange.query.filter_by(id=change_id).first()

    if not change:
        return jsonify({'error': 'Change not found'}), 404

    # Craft the alert message
    alert_message = f"Road changes detected in region: {change.region} on {change.date}."
    
    # Call the alert service to send the email
    send_alert(email, alert_message)

    # Save the alert information in the database
    alert_record = Alert(area_id=change.region, change_detected=True, message=alert_message)
    db.session.add(alert_record)
    db.session.commit()

    return jsonify({'message': 'Alert sent successfully!'})
