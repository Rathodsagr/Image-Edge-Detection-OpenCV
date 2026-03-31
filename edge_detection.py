import cv2

# Read image
image = cv2.imread('input.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Edge detection
edges = cv2.Canny(gray, 100, 200)

# Show images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)

# Save output
cv2.imwrite('edges_output.jpg', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
