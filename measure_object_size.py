import cv2
from object_detector import *
import numpy as np
import cv2.aruco as aruco
from cv2 import aruco


# Load Aruco detector parameters and dictionary
parameters = aruco.DetectorParameters()
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)

# Load object detector
detector = HomogeneousBgDetector()

# Load image
img = cv2.imread("phone_aruco_marker.jpg")
if img is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Get Aruco marker
corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

# Check if any markers were detected
if corners:
    # Draw polygon around the marker with corrected data type
    int_corners = [np.int32(corner) for corner in corners]  # Convert each corner to int32
    cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

    # Aruco perimeter
    aruco_perimeter = cv2.arcLength(corners[0], True)

    # Pixel to cm ratio
    pixel_cm_ratio = aruco_perimeter / 20

    contours = detector.detect_objects(img)

    # Draw objects boundaries
    for cnt in contours:
        # Get rect
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        # Get Width and Height of the Objects by applying the Ratio pixel to cm
        object_width = w / pixel_cm_ratio
        object_height = h / pixel_cm_ratio

        # Display rectangle
        box = cv2.boxPoints(rect)
        box = np.int32(box)  # Corrected line

        cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
        cv2.polylines(img, [box], True, (255, 0, 0), 2)
        cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
        cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
else:
    print("No Aruco markers detected in the image.")
    
