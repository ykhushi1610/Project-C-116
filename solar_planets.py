import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100,100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255,255,200))
cv2.putText(img, "Mercury", (95,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Venus", (185,275), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (290,275), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mars", (380,275), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (500,75), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (750,120), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (950,120), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1090,120), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.imshow("output", img)
cv2.imwrite("Solar_systemwithname.jpg", img)
            
cv2.waitKey(0)
