import cv2
import numpy as np
import os
folder_path = 'E:/Hydroponics/Hydroponics/Rice_Solution/Rice_600/'
def process_image(file_path):
    image = cv2.imread(file_path)
    if image is not None:        
       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
       triangle = cv2.bitwise_not(gray)
       blur = cv2.medianBlur(triangle,5) 
       ret3, binary_image = cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV) 
       ret3, image = cv2.threshold(blur, 0 ,255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE) 
       skeleton_image = cv2.ximgproc.thinning(image)
       distance_transform = cv2.distanceTransform(binary_image, cv2.DIST_L2, 5)
       pixel_size_cm = 0.00423
       surface_area = 0
       for y in range(skeleton_image.shape[0]):
           for x in range(skeleton_image.shape[1]):
               if skeleton_image[y, x] > 0: 
                   radius = distance_transform[y, x] * pixel_size_cm
                   circumference = 2 * np.pi * radius
                   surface_area += circumference
       SA = surface_area * pixel_size_cm
       print(SA)
    else:
        print(f'Error reading.')
for i in range(1, 50): #You can set the number of images for example 1 to 50
    file_name = f'{i}-600.TIF'#Write the file extension after the serially arranged number
    file_path = os.path.join(folder_path, file_name)
    
    process_image(file_path)

