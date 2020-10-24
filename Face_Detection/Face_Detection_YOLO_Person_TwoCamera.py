import cv2
import numpy as np
import time

net = cv2.dnn.readNet("Pre_Model\yolov3.weights", "Pre_Model\yolov3.cfg")
classes = []
with open("Pre_Model\coco.data", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# load input video stream
cap = cv2.VideoCapture(0)
cap2=cv2.VideoCapture(1)
# instantiate a variable 'p' to keep count of persons

# initialize the writer
writer = None
(W, H) = (None, None)
starting_time = time.time()
frame_id = 0
while True:

    ret, frame = cap.read()
    ret, frame2 = cap2.read()
    frame_id += 1
    if W is None or H is None:
        (H, W) = frame.shape[:2]

    # Detecting objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    blob2 = cv2.dnn.blobFromImage(frame2, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    net.setInput(blob2)
    outs = net.forward(output_layers)

    # initialize our lists of detected bounding boxes, confidences, and class IDs, respectively
    boxes = []
    confidences = []
    class_ids = []
    # loop over each of the layer outputs
    for out in outs:

        # loop over each of the detections
        for detection in out:

            # extract the class ID and confidence
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # filter out weak predictions
            if confidence > 0.7:

                center_x = int(detection[0] * W)
                center_y = int(detection[1] * H)
                w = int(detection[2] * W)
                h = int(detection[3] * H)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # update our list of bounding box coordinates, confidences, and class IDs
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.2)

    # detecting persons
    if len(indexes) > 0:
        # loop over the indexes we are keeping
        for i in indexes.flatten():
            # extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            label = str(classes[class_ids[i]])
            if label == 'person':

                # draw a bounding box rectangle and label on the frame
                color = [int(c) for c in colors[class_ids[i]]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.rectangle(frame2, (x, y), (x + w, y + h), color, 2)
                label = "{}: {:.2f}%".format(label, confidence * 100)
                print("predicted object{}".format(label))
                cv2.putText(frame, label,(x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame2, label, (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if writer is None:
                # initialize our video writer

                frame_width = frame.shape[1]
                frame_height = frame.shape[0]
                frame_width2 = frame2.shape[1]
                frame_height2 = frame2.shape[0]
                frame_blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), swapRB=True, crop=False)
                frame_blob2 = cv2.dnn.blobFromImage(frame2, 1 / 255, (416, 416), swapRB=True, crop=False)
            # writer = cv2.VideoWriter(0, fourcc, 30, (frame.shape[1], frame.shape[0]), True)

        elapsed_time = time.time() - starting_time
        fps = frame_id / elapsed_time
        print(str(round(fps, 2)))
        frameCombined = np.hstack((frame, frame2))
        cv2.imshow("Frame", frameCombined)

        if cv2.waitKey(1) == 27:

            break
cap.release()
cap2.release()
cv2.destroyAllWindows()