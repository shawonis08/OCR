import matplotlib.pyplot as plt
import cv2

# img = cv2.imread('image/1.png')
# plt.imshow(img)
# plt.show()

img = cv2.imread('image/1.png')
cimg = img [617:640,22:229]
cv2.imshow("test",cimg)
cv2.waitKey(0)