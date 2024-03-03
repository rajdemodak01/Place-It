import cv2

image = cv2.imread('sample5.jpg', cv2.IMREAD_GRAYSCALE)

def draw_largest_white_rectangle(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Threshold to get binary image
    _, binary_image = cv2.threshold(image, 254.999, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the contour with the largest area
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Get the bounding rectangle of the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)
    
    # Draw the rectangle on the original image
    original_image = cv2.imread('sample5.jpg')
    cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the result
    # cv2.imshow('Largest White Rectangle', original_image)
    cv2.imwrite('dekh_lo.jpg',original_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    place_image = cv2.imread('place_image.jpg')
    
    # Extract the region of interest (ROI) defined by the bounding rectangle
       
    
    
    # Resizing the image 
    resized_roi = cv2.resize(place_image, (w,h))
     
    # Replace the ROI with the resized ROI in the original image
    # image[y:y+h, x:x+w] = resized_roi
    
    
    # Display the result (optional)
    cv2.imwrite('Resized Image.jpg  ', resized_roi)
    original_image[y:y+h, x:x+w] = resized_roi
    cv2.imwrite('done.jpg',original_image)




adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 123, 0.00000008)
cv2.imwrite('output_image.jpg', adaptive_thresh)
image_path='output_image.jpg'
draw_largest_white_rectangle(image_path)
cv2.waitKey(0)
cv2.destroyAllWindows()
