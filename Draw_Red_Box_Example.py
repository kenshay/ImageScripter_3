from elan import *
import numpy as np
import cv2


Viewer.media10items.Click()


with open(r"C:\Settings\Current_Image_Cordinates.txt",'r') as f:
    txt = f.read()
    List = txt.split(',')
    x1 = int(List[0])
    y1 = int(List[1])
    x2 = int(List[2])
    y2 = int(List[3])

print(x1,y1,x2,y2)



img = cv2.imread(r"C:\Settings\Last_Templet_Image.png", 3)
cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()