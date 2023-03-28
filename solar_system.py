import cv2
import numpy as np

solar_img = cv2.imread("solar-system.jpg")
cv2.putText(solar_img, "Sun", (5,300), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 1, color=(255,255,255))
cv2.putText(solar_img, "Mercury", (110,250), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color=(255,255,255))
cv2.putText(solar_img, "Venus", (195,260), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color=(255,255,255))
cv2.putText(solar_img, "Earth", (285,264), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color=(255,255,255))
cv2.putText(solar_img, "Mars", (380,255), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color=(255,255,255))
cv2.putText(solar_img, "Jupiter", (565,380), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color=(255,255,255))
cv2.putText(solar_img, "Saturn", (780,315), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color=(255,255,255))
cv2.putText(solar_img, "Uranus", (970,292), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color=(255,255,255))
cv2.putText(solar_img, "Neptune", (1112,287), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color=(255,255,255))
cv2.imwrite("Solar_planets_name.jpg",solar_img)
cv2.imshow("Display Window", "Solar_planets_name.jpg")
cv2.waitKey(0)