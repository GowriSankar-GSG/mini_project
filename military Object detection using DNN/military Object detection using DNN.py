import cv2
import urllib.request
from gui_buttons import Buttons
import numpy as np
import json

#Intialize Buttons
button = Buttons()
button.add_button("soldier", 20,20)
button.add_button("car", 20, 90)

button.add_button("bus", 20, 155)
button.add_button("truck", 20, 230)
button.add_button("aircraft", 20, 300)
button.add_button("all", 20, 370)


# Opencv DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
#gving parameter for yolo4 DNN model because every type has different parameters
model.setInputParams(size=(320,320),scale=1/255)

#Load class lists
classes = []
with open("dnn_model/classes.txt","r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
print("Object list")
print(classes)


#Intialize camera
URL = "http://192.168.43.1:8080/shot.jpg"
#Full HD 1920 x 1080

#Geo Location
location = "http://ipinfo.io/json"
response = urllib.request.urlopen(location)
data = json.load(response)


def click_button(event,x,y,flags,params):
    global button_person
    if event == cv2.EVENT_LBUTTONDOWN:
        button.button_click(x,y)




#Create window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click_button) ,

while True:
    #get frame
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)

    active_buttons = button.active_buttons_list()
    print("Active buttons", active_buttons)



    #object detection
    (class_ids, scores,bboxes) = model.detect(frame)
    for class_id, score,bbox in zip(class_ids,scores,bboxes):
        (x,y,w,h) = bbox
        class_name=classes[class_id]


        #enable button
        if str("all") in  active_buttons:
            # put text
            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            # draw rectangle on frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 50), 3)

        elif class_name in active_buttons:
            # put text
            class_name= class_name+" --->Alert"
            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            # draw rectangle on frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 50), 3)
            print(data)


   # print("class ids", class_ids)
    #print("scores", scores)
    #print("bboxes",bboxes)

    #display button
    button.display_buttons(frame
                           )


    cv2.imshow("Frame", frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()