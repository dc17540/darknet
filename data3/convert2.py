
k = open("test2.txt","w")
z = open("train2.txt","w")

#for i in range(0,394):
   # x.write(str(i+1)+".txt" +"\n")


#x.close()

theList = []
theFinList = []

import os
y =os.listdir("/home/dr_dunstan/makeItHappen/attempt1/anno/Yolo-Annotation-Tool-New-/Images/vid1F2/")
print(y)


for element in y:
    if(element[len(element)-1] == "t"):
        if(os.path.isfile(element)):
            x = open(element)
            theList = []
            for line in x:
                theList.append(line)
            if(len(theList) != 0):
                theFinList.append(element[0:len(element)-3] +"jpg" +"\n")

counter = 0
for line in theFinList:
    if(counter % 10 == 0):
        k.write("/content/darknet/data3/" +line)
    else:
        z.write("/content/darknet/data3/"+line)
    counter += 1
k.close()
z.close()

