import cv2

path = "resources/google.jpg"
img = cv2.imread(path)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("image", img)
cv2.imshow("greyImage", grey_img)

cv2.waitKey(0)