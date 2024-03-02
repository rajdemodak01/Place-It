import cv2

# Read the image in grayscale
image = cv2.imread('sample4.jpg', cv2.IMREAD_GRAYSCALE)

def draw_largest_white_rectangle(image_path):
    # Read the image
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
    original_image = cv2.imread('sample4.jpg')
    cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the result
    cv2.imshow('Largest White Rectangle', original_image)
    cv2.imwrite('dekh_lo.jpg',original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Apply adaptive thresholding
# Parameters:
#   src: Input image
#   maxValue: Maximum intensity value that will be assigned to the pixel values exceeding the threshold
#   adaptiveMethod: Method used to calculate the threshold. It can be cv2.ADAPTIVE_THRESH_MEAN_C or cv2.ADAPTIVE_THRESH_GAUSSIAN_C
#   thresholdType: Type of thresholding. It can be cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV
#   blockSize: Size of the local region around each pixel to calculate the threshold value (odd number)
#   C: Constant subtracted from the mean or weighted mean
adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 123, 0.00000008)

# Display the original and thresholded images
# cv2.imshow('Original Image', image)
# cv2.imshow('Adaptive Thresholded Image', adaptive_thresh)
cv2.imwrite('output_image.jpg', adaptive_thresh)
image_path='output_image.jpg'
draw_largest_white_rectangle(image_path)
cv2.waitKey(0)
cv2.destroyAllWindows()
