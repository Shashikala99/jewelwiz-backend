import cv2
from object_detector import *
import numpy as np

# Load Aruco detector
parameters = cv2.aruco
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
img = cv2.imread("phone.jpg")


# Load Object Detector
detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)
print(contours)
'''
# Load Image
img = cv2.imread("phone_aruco_marker.jpg")

# Get Aruco marker
#corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

# Draw polygon around the marker
int_corners = np.int0(corners)
cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

# Aruco Perimeter
aruco_perimeter = cv2.arcLength(corners[0], True)

# Pixel to cm ratio
pixel_cm_ratio = aruco_perimeter / 20

contours = detector.detect_objects(img)
'''

corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
int_corners = np.int0(corners)
cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

aruco_perimeter = cv2.arcLength(corners[0], True)
pixel_cm_ratio = aruco_perimeter / 20
# Draw objects boundaries

for cnt in contours:
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Get Width and Height of the Objects by applying the Ratio pixel to cm
    #object_width = w / pixel_cm_ratio
    #object_height = h / pixel_cm_ratio

    # Display rectangle
    #box = cv2.boxPoints(rect)
   # box = np.int0(box)

   # cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

   #draw polygon
    cv2.polylines(img, [cnt], True, (255, 0, 0), 2)

    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

# Get Width and Height of the Objects by applying the Ratio pixel to cm
    object_width = w / pixel_cm_ratio
    object_height = h / pixel_cm_ratio

    
 # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int32(box)

    
    
    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], isClosed=True, color=(255, 0, 0), thickness=2)

    

   

    cv2.putText(img, "Width {} cm".format(w), (int(x), int(y)), cv2.FONT_HERSHEY_PLAIN, 1, (100, 200, 0), 2)
    #cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)


cv2.imshow("Image", img)
cv2.waitKey(0)