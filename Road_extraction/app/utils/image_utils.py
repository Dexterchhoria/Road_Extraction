import cv2

def save_composite_image(image, filename):
    """
    Saves the processed image to a file.
    
    Args:
        image (np.ndarray): Image to be saved.
        filename (str): File name for the saved image.
    """
    cv2.imwrite(filename, image)
    print(f"Image saved as {filename}")
