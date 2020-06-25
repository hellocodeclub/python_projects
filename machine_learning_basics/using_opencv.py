import cv2

image = cv2.imread('img.jpg')

#splitting into different channels
#(b,g,r) = cv2.split(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cas_alt2 = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cas_default = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces=cas_alt2.detectMultiScale(gray)
#img_faces_alt2 = show_detection(image.copy(), faces_alt2)


for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow('Loaded image',image)
cv2.imwrite('result.jpeg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()



#noise removal
#image sharpening
#illumination
