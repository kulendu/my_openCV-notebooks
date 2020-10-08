import cv2
import numpy as np

cam = cv2.VideoCapture(0)


def empty(a):
    pass


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",700,250)
cv2.createTrackbar("Hue min","HSV",0,179,empty)
cv2.createTrackbar("Hue max","HSV",179,179,empty)
cv2.createTrackbar("saturation min","HSV",0,255,empty)
cv2.createTrackbar("saturation max","HSV",255,255,empty)
cv2.createTrackbar("val min","HSV",0,255,empty)
cv2.createTrackbar("val max","HSV",255,255,empty)


while True:

    _, frame = cam.read()
    
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hue_min = cv2.getTrackbarPos("Hue min","HSV")
    hue_max = cv2.getTrackbarPos("Hue max","HSV")
    sat_min = cv2.getTrackbarPos("saturation min","HSV")
    sat_max = cv2.getTrackbarPos("saturation max","HSV")
    val_min = cv2.getTrackbarPos("val min","HSV")
    val_max = cv2.getTrackbarPos("val min","HSV")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(hsv_img, lower, upper)
    final_img = cv2.bitwise_and(frame,frame, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    h_stack = np.hstack([frame, mask, final_img])


    # cv2.imshow("camera", frame)
    # cv2.imshow("hsvImage", hsv_img)
    # cv2.imshow("mask", mask)
    # cv2.imshow("final", mask)
    cv2.imshow("final img", h_stack)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break