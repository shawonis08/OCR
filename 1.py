import cv2
list1 =[]

img = cv2.imread('image/bar.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray, 47, 255, cv2.THRESH_BINARY)

C, H, W = img.shape[::-1]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray, 47, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(thresh[:, 0:H, ], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    perimeter = cv2.arcLength(contours[i], True)
    if perimeter >0 and perimeter <80:
        cv2.drawContours (img, contours, i, (0, 255, 0), 2)
        list1.append(i)

cv2.imshow('thresh',img)
cv2.waitKey(0)



# img = cv2.imread('image/1.png')
# cimg = img [617:640,22:229]
# cv2.imshow("test",cimg)
# cv2.waitKey(0)
# cv2.imwrite('image/bar.png',cimg)