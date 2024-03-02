import cv2

def find_and_draw_largest_blank_space(image_path):
    """Finds the largest blank white space and draws a rectangle around it.

    Args:
        image_path (str): Path to the image.
    """

    # Load and convert to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Adjust thresholds as needed
    lower_white = 230
    upper_white = 255

    # Apply thresholding
    thresh = cv2.threshold(gray, lower_white, upper_white, cv2.THRESH_BINARY)[1]

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter and find the largest contour
    min_area = 0.01 * image.shape[0] * image.shape[1]
    large_contours = [c for c in contours if cv2.contourArea(c) >= min_area]

    if large_contours:
        largest_contour = max(large_contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Draw the rectangle 
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('Image with Rectangle', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No significant blank space found.")

# Example usage:
image_path = 'savedimage.jpg'  # Replace with the path to your image
find_and_draw_largest_blank_space(image_path)
