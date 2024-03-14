import cv2
img = cv2.imread('bimg.jpg')
# Draw the body
cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 0), 2)

# Draw the head
cv2.circle(img, (200, 70), 30, (0, 0, 0), 2)

# Draw the eyes
cv2.circle(img, (180, 60), 5, (0, 0, 0), -1)
cv2.circle(img, (220, 60), 5, (0, 0, 0), -1)

# Draw the arms
cv2.line(img, (100, 150), (50, 200), (0, 0, 0), 2)
cv2.line(img, (300, 150), (350, 200), (0, 0, 0), 2)

# Draw the legs
cv2.line(img, (150, 300), (100, 350), (0, 0, 0), 2)
cv2.line(img, (250, 300), (300, 350), (0, 0, 0), 2)

# Display the image
cv2.imshow('Robot', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
