import cv2
img = cv2.imread('bimg.jpeg')
color = (0,255,0)

#Circle
coordinates = (256,256)
radius = 50
thickness = 2

#rectangle
start=(150,150)
end=(400,350)

#square
start1=(50,50)
end1=(100,100)


cv2.circle(img,coordinates,radius,color,thickness)
cv2.rectangle(img,start,end,color,thickness)
cv2.rectangle(img,start1,end1,color,thickness)
cv2.imshow('circle',img)
cv2.waitKey(0)
