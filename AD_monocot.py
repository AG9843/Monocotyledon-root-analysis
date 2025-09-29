import cv2
import numpy as np
import os

folder_path = 'F:/Hydroponics/Hydroponics/Wheat_Solution/600DPI/'

def process_image(file_path):

    image = cv2.imread(file_path)
    if image is not None:
        
       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

       triangle = cv2.bitwise_not(gray)
       blur = cv2.medianBlur(triangle,5) 
       ret3, binary_image = cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV) 
       ret3, image = cv2.threshold(blur, 0 ,255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE) 
       skeleton_image = cv2.ximgproc.thinning(image)
       num_components, labels, stats, centroids = cv2.connectedComponentsWithStats(skeleton_image) 
       length = stats[:, cv2.CC_STAT_AREA]
       length = list(sorted(length))
       assert len(length) >= 2
       total_length = 0
       noise = 250
       for i, length in enumerate(length[:-1]):
           if length > noise:
               total_length += length
               TRL = total_length 
       pixel_size_cm = 0.00423 
       distance_transform = cv2.distanceTransform(binary_image, cv2.DIST_L2, 5)
       diameter_sum = 0

       for y in range(skeleton_image.shape[0]):
           for x in range(skeleton_image.shape[1]):
               if skeleton_image[y, x] > 0:  # Check if the pixel is part of the skeleton
                   radius = distance_transform[y, x] * pixel_size_cm
                   diameter = 2 * radius
                   diameter_sum += diameter
       average_diameter = diameter_sum / TRL
       print(average_diameter)
    else:
        print(f'Error reading {file_path}.')

for i in range(1, 50): #You can set the number of images for example 1 to 50
    file_name = f'{i}_600.TIF'#Write the file extension after the serially arranged number
    file_path = os.path.join(folder_path, file_name)
    
    process_image(file_path)

