import cv2
a=cv2.imread('image.jpg',cv2.IMREAD_UNCHANGED)
scale_percent=50
width=int(a.shape[1]*scale_percent/100)
heigth=int(a.shape[0]*scale_percent/100)
dsize=(width,heigth)
output=cv2.resize(a,dsize)
d=cv2.imwrite("Resized Image",output)
cv2.imshow("Resized Image",d)
cv2.waitKey(0)
