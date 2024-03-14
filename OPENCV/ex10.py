import cv2
import numpy as np
image = cv2.imread('a.png')
height, width = image.shape[:2]
tx,ty = width / 4, height / 4
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)
translated_image = cv2.warpAffine(src=image, M=translation_matrix, dsize=(width, height))
cv2.imshow('Translated image', translated_image)
cv2.imshow('Original image', image)
cv2.waitKey(0)
cv2.imwrite('translated_n.jpg', translated_image)