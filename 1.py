import cv2

img = cv2.imread('image/1.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray, 47, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)



img = cv2.imread('image/1.png')
cimg = img [617:640,22:229]
cv2.imshow("test",cimg)
cv2.waitKey(0)
cv2.imwrite('image/bar.png',cimg)
