import cv2
import numpy as np
import rasterio
import smtplib
from email.mime.text import MIMEText

# Function to read and merge Band TIFF files into a color composite
def read_bands_to_composite(band2_path, band3_path, band4_path):
    """
    Reads individual band TIFF files and creates a false-colored composite image.
    
    Args:
        band2_path (str): Path to the blue band TIFF file.
        band3_path (str): Path to the green band TIFF file.
        band4_path (str): Path to the red band TIFF file.

    Returns:
        np.ndarray: Color composite image normalized to 0-255 range.
    """
    with rasterio.open(band2_path) as band2, \
         rasterio.open(band3_path) as band3, \
         rasterio.open(band4_path) as band4:

        # Read each band into separate arrays
        band2_data = band2.read(1)  # Blue band
        band3_data = band3.read(1)  # Green band
        band4_data = band4.read(1)  # Red band

        # Stack the bands to create a color composite (Red, Green, Blue)
        composite = np.dstack((band4_data, band3_data, band2_data))

        # Normalize composite to the range 0-255 for image display
        composite = np.clip(composite, 0, 255)
        composite = composite.astype(np.uint8)

    return composite

# Function to resize image to match another image's size
def resize_to_match(image1, image2):
    """
    Resizes the second image to match the size of the first image.

    Args:
        image1 (np.ndarray): Reference image.
        image2 (np.ndarray): Image to be resized.

    Returns:
        np.ndarray: Resized image.
    """
    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]
    
    if (height1, width1) != (height2, width2):
        image2 = cv2.resize(image2, (width1, height1), interpolation=cv2.INTER_AREA)
    
    return image2

# Function to extract roads using edge detection and morphological operations
def extract_roads(image):
    """
    Extracts road features from the image using edge detection and morphological operations.

    Args:
        image (np.ndarray): Color composite image.

    Returns:
        np.ndarray: Binary image with extracted roads.
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)  # Larger kernel size for more smoothing

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, 30, 100)  # Adjust thresholds based on image

    # Morphological operations to refine the edges
    kernel = np.ones((9, 9), np.uint8)  # Larger kernel for better connectivity
    dilated = cv2.dilate(edges, kernel, iterations=2)
    closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    return closed

# Function to detect changes between old and new road images
def detect_changes(old_roads, new_roads):
    """
    Detects changes between the old and new road images.

    Args:
        old_roads (np.ndarray): Binary image with roads from the old image.
        new_roads (np.ndarray): Binary image with roads from the new image.

    Returns:
        np.ndarray: Binary image highlighting detected changes.
    """
    # Compute absolute difference between old and new road images
    difference = cv2.absdiff(old_roads, new_roads)

    # Threshold the difference image to highlight significant changes
    _, change_mask = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)  # Adjust threshold value

    return change_mask

# Function to generate an email alert
def send_alert(email_address, message):
    """
    Sends an email alert about detected road changes.

    Args:
        email_address (str): Recipient email address.
        message (str): Message content to be sent.
    """
    msg = MIMEText(message)
    msg['Subject'] = 'Road Network Change Alert'
    msg['From'] = 'noreply@roadsystem.com'
    msg['To'] = email_address

    smtp_server = 'smtp.your-email-provider.com'
    smtp_port = 587  # Use 465 for SSL or 587 for TLS

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade connection to secure SSL/TLS
            server.login('your-email@provider.com', 'your-password')
            server.sendmail('noreply@roadsystem.com', email_address, msg.as_string())
            print("Alert email sent!")
    except smtplib.SMTPConnectError:
        print("Failed to connect to the SMTP server.")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate with the SMTP server.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

# Function to save images
def save_composite_image(image, filename):
    """
    Saves the processed image to a file.

    Args:
        image (np.ndarray): Image to be saved.
        filename (str): File name for the saved image.
    """
    cv2.imwrite(filename, image)
    print(f"Image saved as {filename}")

# Main function to process old and new images and detect road changes
def process_images_and_detect_changes(old_band_paths, new_band_paths, email_address):
    """
    Processes old and new images, extracts roads, detects changes, and sends an alert if changes are detected.

    Args:
        old_band_paths (tuple): Paths to the TIFF files of the old image bands (B2, B3, B4).
        new_band_paths (tuple): Paths to the TIFF files of the new image bands (B2, B3, B4).
        email_address (str): Email address to send alerts.
    """
    # Read and process the old and new images
    old_image = read_bands_to_composite(*old_band_paths)
    new_image = read_bands_to_composite(*new_band_paths)

    # Ensure both images have the same size
    new_image_resized = resize_to_match(old_image, new_image)

    # Save the false-colored composite images
    save_composite_image(old_image, 'old_image_composite.png')
    save_composite_image(new_image_resized, 'new_image_composite.png')

    # Extract roads from both images
    old_roads = extract_roads(old_image)
    new_roads = extract_roads(new_image_resized)

    # Save the road extraction results
    save_composite_image(old_roads, 'old_roads_extracted.png')
    save_composite_image(new_roads, 'new_roads_extracted.png')

    # Detect changes (new roads or lost roads)
    changes = detect_changes(old_roads, new_roads)

    # Save the change detection result
    save_composite_image(changes, 'road_changes_detected.png')

    # Display the extracted roads and the detected changes
    cv2.imshow('Old Roads', old_roads)
    cv2.imshow('New Roads', new_roads)
    cv2.imshow('Changes Detected', changes)

    # Check if any significant changes were detected
    if np.count_nonzero(changes) > 0:
        alert_message = "New road developments or road losses have been detected."
        send_alert(email_address, alert_message)

    # Wait for user input to close image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
old_band_paths = ('BAND2.tif', 'BAND3.tif', 'BAND4.tif')
new_band_paths = ('BAND2_sep.tif', 'BAND3_sep.tif', 'BAND4_sep.tif')
email_address = 'eishaankhatri@gmail.com'

process_images_and_detect_changes(old_band_paths, new_band_paths, email_address)
