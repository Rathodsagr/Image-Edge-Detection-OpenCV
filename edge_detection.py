import cv2

# Load the input image
image = cv2.imread('input.jpg')

# Check if image loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Save output image
cv2.imwrite('edges_output.jpg', edges)

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
