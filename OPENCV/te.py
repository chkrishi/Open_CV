import cv2
import stasm
from matplotlib import pyplot as plt
img = cv2.imread('Face1.jpg', cv2.IMREAD_GRAYSCALE)
landmarks = stasm.search_single(img)
print(f'landmarks count = {len(landmarks)}')
fig = plt.figure(figsize=(16, 10))
ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(img, cmap='gray')

for pt in landmarks:
  cv2.circle(img, (pt[0], pt[1]), 5, (0, 0, 255), -1)

ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(img, cmap='gray')
