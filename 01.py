# Importing the OpenCV library 
import cv2 
#importing os module for saving the file after done
# import os
# Reading the image using imread() function 
image = cv2.imread('image.jpg') 

# Extracting the height and width of an image 
h, w = image.shape[:2] 
# Displaying the height and width 
print("Height = {}, Width = {}".format(h, w)) 


#################################
# resize() function takes 2 parameters, 
# the image and the dimensions 
resize = cv2.resize(image, (800, 800)) 
#################################

#################################
# The problem with this approach is that the aspect ratio of the image is not maintained. So we need to do some extra work in order to maintain a proper aspect ratio.

# Calculating the ratio 
# ratio = 800 / w 

# # Creating a tuple containing width and height 
# dim = (800, int(h * ratio)) 

# # Resizing the image 
# resize = cv2.resize(image, dim) 
###############################


#################################
#for Rotating the Image
# Calculating the center of the image 
# center = (w // 2, h // 2) 

# # Generating a rotation matrix 
# matrix = cv2.getRotationMatrix2D(center, -45, 1.0) 

# # Performing the affine transformation 
# rotated = cv2.warpAffine(image, matrix, (w, h)) 
#################################

# Window name in which image is displayed 
window_name = 'image'
  
# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name, resize) 

filename = 'savedImage.jpg'
  
# Using cv2.imwrite() method 
# Saving the image 
cv2.imwrite(filename, resize) 

# waits for user to press any key 
# (this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(0) 
  
# closing all open windows 
cv2.destroyAllWindows() 

