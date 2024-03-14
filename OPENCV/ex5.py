import cv2
a=cv2.imread('image.jpg')
cv2.imshow('JPEG-LOGO',a)
height=a.shape[0]
width=a.shape[1]
print("Image height =",height)
print("Image height =",width)
cv2.waitKey(0)
