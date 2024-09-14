from flask import Blueprint, jsonify, request
from app.services.image_processing_service import download_images

gateway_bp = Blueprint('gateway', __name__)

@gateway_bp.route('/download', methods=['GET'])
def download_image():
    aoi = request.args.get('aoi')
    download_images(aoi)
    return jsonify({"message": f"Images for {aoi} downloaded successfully."})
