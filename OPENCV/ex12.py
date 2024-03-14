import cv2
img = cv2.imread('bimg.jpg')
coordinates = (250, 250)
radius = 150

color = (0, 0, 255)
color2 = (255,255,255)
color3= (0, 0, 255)
thickness = 2

# Draw face outline
cv2.circle(img, coordinates, radius, color, thickness)

# Draw left eye
cv2.circle(img, (200, 200), 20, color2, thickness)

# Draw right eye
cv2.circle(img, (300, 200), 20, color2, thickness) 

# Draw mouth
cv2.rectangle(img, (200, 300), (300, 320), color3, thickness) 

# Display the image
cv2.imshow('Human Face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
