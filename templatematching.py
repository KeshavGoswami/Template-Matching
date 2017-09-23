import cv2
import numpy as np

img=cv2.imread('C:\Users\Keshav Goswami\Desktop\Softwares\opencv\IRONman\IRONMAN.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

temp=cv2.imread('C:\Users\Keshav Goswami\Desktop\Softwares\opencv\IRONman\iron2.PNG',0)
w,h=temp.shape[::-1]

result=cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED)
threshold=0.85

loc=np.where(result>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),0)

cv2.imshow('detected',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



