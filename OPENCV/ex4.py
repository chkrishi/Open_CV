import cv2
a=cv2.imread('image.jpg')
cv2.imshow("JPEG IMAGE",a)
b=cv2.imread('a.png')
cv2.imshow("PNG IMAGE",b)
c=cv2.imread('b.tiff')
cv2.imshow("TIFF IMAGE",c)
cv2.waitKey(0)
