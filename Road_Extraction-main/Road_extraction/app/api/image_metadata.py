from flask import Blueprint, request, jsonify
from app.utils.database_utils import db  # Import your database instance
from app.models import ImageMetadata  # Import your ImageMetadata model

# Create the image metadata blueprint
image_metadata_bp = Blueprint('image_metadata', __name__)

@image_metadata_bp.route('/add', methods=['POST'])
def add_image_metadata():
    data = request.json
    try:
        new_image = ImageMetadata(
            product_id=data.get('product_id'),
            ots_product_id=data.get('ots_product_id'),
            sat_id=data.get('sat_id'),
            sensor=data.get('sensor'),
            sub_scene=data.get('sub_scene'),
            gen_agency=data.get('gen_agency'),
            path=data.get('path'),
            row_number=data.get('row_number'),
            segment_number=data.get('segment_number'),
            session_number=data.get('session_number'),
            strip_number=data.get('strip_number'),
            scene_number=data.get('scene_number'),
            date_of_pass=data.get('date_of_pass'),
            no_of_bands=data.get('no_of_bands'),
            band_numbers=data.get('band_numbers'),
            pass_type=data.get('pass_type'),
            date_of_dump=data.get('date_of_dump'),
            dumping_orbit_no=data.get('dumping_orbit_no'),
            imaging_orbit_no=data.get('imaging_orbit_no'),
            bytes_per_pixel=data.get('bytes_per_pixel'),
            bits_per_pixel=data.get('bits_per_pixel'),
            generation_date_time=data.get('generation_date_time'),
            prod_code=data.get('prod_code'),
            prod_type=data.get('prod_type'),
            input_resolution_along=data.get('input_resolution_along'),
            input_resolution_across=data.get('input_resolution_across'),
            output_resolution_along=data.get('output_resolution_along'),
            output_resolution_across=data.get('output_resolution_across'),
            season=data.get('season'),
            image_format=data.get('image_format'),
            processing_level=data.get('processing_level'),
            resamp_code=data.get('resamp_code'),
            no_scans=data.get('no_scans'),
            no_pixels=data.get('no_pixels'),
            start_pixel=data.get('start_pixel'),
            map_projection=data.get('map_projection'),
            ellipsoid=data.get('ellipsoid'),
            datum=data.get('datum'),
            map_origin_lat=data.get('map_origin_lat'),
            map_origin_lon=data.get('map_origin_lon'),
            prod_ul_lat=data.get('prod_ul_lat'),
            prod_ul_lon=data.get('prod_ul_lon'),
            prod_u_lat=data.get('prod_u_lat'),
            prod_u_lon=data.get('prod_u_lon'),
            prod_lr_lat=data.get('prod_lr_lat'),
            prod_lr_lon=data.get('prod_lr_lon'),
            prod_ll_lat=data.get('prod_ll_lat'),
            prod_ll_lon=data.get('prod_ll_lon'),
            image_ul_lat=data.get('image_ul_lat'),
            image_ul_lon=data.get('image_ul_lon'),
            image_u_lat=data.get('image_u_lat'),
            image_u_lon=data.get('image_u_lon'),
            image_lr_lat=data.get('image_lr_lat'),
            image_lr_lon=data.get('image_lr_lon'),
            image_ll_lat=data.get('image_ll_lat'),
            image_ll_lon=data.get('image_ll_lon'),
            prod_ul_map_x=data.get('prod_ul_map_x'),
            prod_ul_map_y=data.get('prod_ul_map_y'),
            prod_ur_map_x=data.get('prod_ur_map_x'),
            prod_ur_map_y=data.get('prod_ur_map_y'),
            prod_lr_map_x=data.get('prod_lr_map_x'),
            prod_lr_map_y=data.get('prod_lr_map_y'),
            prod_ll_map_x=data.get('prod_ll_map_x'),
            prod_ll_map_y=data.get('prod_ll_map_y'),
            scene_center_lat=data.get('scene_center_lat'),
            scene_center_lon=data.get('scene_center_lon'),
            standard_parallel_1=data.get('standard_parallel_1'),
            standard_parallel_2=data.get('standard_parallel_2'),
            false_easting=data.get('false_easting'),
            false_northing=data.get('false_northing'),
            zone_no=data.get('zone_no'),
            scene_center_time=data.get('scene_center_time'),
            scene_center_roll=data.get('scene_center_roll'),
            scene_center_pitch=data.get('scene_center_pitch'),
            scene_center_yaw=data.get('scene_center_yaw'),
            sun_azimuth_at_center=data.get('sun_azimuth_at_center'),
            sun_elevation_at_center=data.get('sun_elevation_at_center'),
            image_heading_angle=data.get('image_heading_angle'),
            incidence_angle=data.get('incidence_angle'),
            satellite_altitude=data.get('satellite_altitude'),
            tilt_angle=data.get('tilt_angle'),
            dem_correction=data.get('dem_correction'),
            source_of_orbit=data.get('source_of_orbit'),
            source_of_attitude=data.get('source_of_attitude'),
            imaging_direction=data.get('imaging_direction'),
            b2_temp=data.get('b2_temp'),
            b3_temp=data.get('b3_temp'),
            b4_temp=data.get('b4_temp'),
            b2_lmin=data.get('b2_lmin'),
            b3_lmin=data.get('b3_lmin'),
            b4_lmin=data.get('b4_lmin'),
            b2_lmax=data.get('b2_lmax'),
            b3_lmax=data.get('b3_lmax'),
            b4_lmax=data.get('b4_lmax'),
            quality=data.get('quality'),
            cloud_percent=data.get('cloud_percent'),
            across_track_accuracy=data.get('across_track_accuracy'),
            along_track_accuracy=data.get('along_track_accuracy'),
            shift_percent=data.get('shift_percent'),
            satellite_heading_angle=data.get('satellite_heading_angle'),
            scene_start_time=data.get('scene_start_time'),
            scene_end_time=data.get('scene_end_time'),
            sen_azimuth_at_center=data.get('sen_azimuth_at_center'),
            sen_elevation_at_center=data.get('sen_elevation_at_center'),
            incidence_angle_along_track=data.get('incidence_angle_along_track'),
            incidence_angle_across_track=data.get('incidence_angle_across_track'),
            view_angle=data.get('view_angle'),
            view_angle_along_track=data.get('view_angle_along_track'),
            view_angle_across_track=data.get('view_angle_across_track'),
            product_scene_start_time=data.get('product_scene_start_time'),
            product_scene_end_time=data.get('product_scene_end_time'),
            jpeg_no_columns=data.get('jpeg_no_columns'),
            jpeg_no_rows=data.get('jpeg_no_rows'),
        )
        db.session.add(new_image)
        db.session.commit()
        return jsonify({"message": "Image metadata added successfully!"}), 201
    except Exception as e:
        print(f"Error adding image metadata: {e}")  # Log the error for debugging
        return jsonify({"error": str(e)}), 400

@image_metadata_bp.route('/', methods=['GET'])
def get_image_metadata():
    try:
        images = ImageMetadata.query.all()
        return jsonify([image.to_dict() for image in images]), 200
    except Exception as e:
        print(f"Error retrieving images: {e}")  # Log the error for debugging
        return jsonify({"error": str(e)}), 500
