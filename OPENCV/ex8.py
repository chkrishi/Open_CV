import cv2
a=cv2.imread('image.jpg')
b=cv2.rotate(a, cv2.ROTATE_90_CLOCKWISE)
c=cv2.rotate(a, cv2.ROTATE_180)
d=cv2.rotate(a, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Image 90",b)
cv2.imshow("Image 180",c)
cv2.imshow("Image counter 90",d)
cv2.waitKey(0)
