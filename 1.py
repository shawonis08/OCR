import cv2
import matplotlib.pyplot as plt
list1 =[]

img = cv2.imread('image/bar.png')
# t = plot.imread('image/bar.png')

C, H, W = img.shape[::-1]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray, 47, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(thresh[:, 0:H, ], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    perimeter = cv2.arcLength(contours[i], True)
    if perimeter >0 and perimeter <80:
        cv2.drawContours (img, contours, i, (0, 255, 0), 1)
        list1.append(i)

t = 0
while t<200:
    cv2.imwrite('%d.png'%t, img[2:20, t:t+20])
    t+=20




    # plot.imshow(t)
# plot.show()



# for x in list1:
#     M = cv2. moments(contours[x])
#     cx = int(M['m10']/M['m00'])
#     cy = int(M['m01'] / M['m00'])
#     cv2.rectangle(img, (cx-10, cy-10),(cx+10, cy+10), (0, 255, 255), 2)
#     cropped = img[cy - 10:cy + 10, cx - 10:cx + 10]
#     cv2.imshow('cropped', cropped)


# h,w = thresh.shape
# print(w)
# cv2.imshow('thresh',img)
# cv2.waitKey(0)



# img = cv2.imread('image/1.png')
# cimg = img [617:640,22:229]
# cv2.imshow("test",cimg)
# cv2.waitKey(0)
# cv2.imwrite('image/bar.png',cimg)