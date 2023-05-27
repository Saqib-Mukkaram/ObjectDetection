# importng dependacies
import cv2
from matplotlib import pyplot as plt

net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights",
                      "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)
#loading text ojects from the txt
classes = []
with open("dnn_model/classes.txt","r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
#connecting with camera
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('http://192.168.18.9:4747/video')

# loop runs if capturing has been initialized
while (1):

    # reads frame from a camera
    ret, frame = cap.read()
    
    (class_ids, scores, bboxes) = model.detect(frame)
    
    for class_id ,score , bbox in zip(class_ids,scores,bboxes):
        (x,y,w,h) = bbox
        print(x,y,w,h)
        class_name = classes[class_id]
        cv2.putText(frame,str(class_name),(x,y-5),cv2.FONT_HERSHEY_PLAIN,3,(200,200,200),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,0,50),3)
    
    
    # print(f"class_ids {class_ids}")
    # print(f"scores: {scores}")
    # print(f"bboxes {bboxes}")
    # Display the frame
    cv2.imshow('Camera', frame)
    # Wait for 25ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera from video capture
cap.release()
