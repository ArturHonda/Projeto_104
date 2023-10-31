import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,"mercurio",(110,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"venus",(190,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"terra",(280,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"marte",(380,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"jupter",(480,70),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"saturno",(720,110),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"urano",(950,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"netuno",(1080,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("sistema solar",img)
cv2.waitKey(0)