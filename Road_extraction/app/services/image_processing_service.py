import cv2
import numpy as np
import rasterio
from app.services.alert_service import send_alert
from app.utils.image_utils import save_composite_image

def read_bands_to_composite(band2_path, band3_path, band4_path):
    # Your original code for reading bands and creating a composite image
    with rasterio.open(band2_path) as band2, \
         rasterio.open(band3_path) as band3, \
         rasterio.open(band4_path) as band4:

        band2_data = band2.read(1)
        band3_data = band3.read(1)
        band4_data = band4.read(1)

        composite = np.dstack((band4_data, band3_data, band2_data))
        composite = np.clip(composite, 0, 255).astype(np.uint8)

    return composite

def resize_to_match(image1, image2):
    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]

    if (height1, width1) != (height2, width2):
        image2 = cv2.resize(image2, (width1, height1), interpolation=cv2.INTER_AREA)

    return image2

def extract_roads(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blurred, 30, 100)
    
    kernel = np.ones((9, 9), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=2)
    closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    
    return closed

def detect_changes(old_roads, new_roads):
    difference = cv2.absdiff(old_roads, new_roads)
    _, change_mask = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)
    
    return change_mask

def process_images_and_detect_changes(old_band_paths, new_band_paths, email_address):
    old_image = read_bands_to_composite(*old_band_paths)
    new_image = read_bands_to_composite(*new_band_paths)

    new_image_resized = resize_to_match(old_image, new_image)

    save_composite_image(old_image, 'old_image_composite.png')
    save_composite_image(new_image_resized, 'new_image_composite.png')

    old_roads = extract_roads(old_image)
    new_roads = extract_roads(new_image_resized)

    save_composite_image(old_roads, 'old_roads_extracted.png')
    save_composite_image(new_roads, 'new_roads_extracted.png')

    changes = detect_changes(old_roads, new_roads)
    save_composite_image(changes, 'road_changes_detected.png')

    if np.count_nonzero(changes) > 0:
        alert_message = "New road developments or road losses have been detected."
        send_alert(email_address, alert_message)

