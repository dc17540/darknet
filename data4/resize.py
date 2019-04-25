from PIL import Image
import sys
import os
x = os.listdir("/home/dr_dunstan/makeItHappen/attempt1/anno/Yolo-Annotation-Tool-New-/Images/theFinal")
for element in x:
    print(element)
    filename = element
    basewidth = 720
    img = Image.open(element)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(filename) 
