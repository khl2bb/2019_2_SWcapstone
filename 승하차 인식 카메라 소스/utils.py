# *******************************************************************
#
# Author : Thanh Nguyen, 2018
# Email  : sthanhng@gmail.com
# Github : https://github.com/sthanhng
#
# BAP, AI Team
# Face detection using the YOLOv3 algorithm
#
# Description : utils.py
# This file contains the code of the parameters and help functions
#
# *******************************************************************


import datetime
import numpy as np
import cv2

# -------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------

CONF_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4
IMG_WIDTH = 416
IMG_HEIGHT = 416

# Default colors
COLOR_BLUE = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (0, 255, 255)


# -------------------------------------------------------------------
# Help functions
# -------------------------------------------------------------------

# Get the names of the output layers
def get_outputs_names(net):
    # Get the names of all the layers in the network
    layers_names = net.getLayerNames()

    # Get the names of the output layers, i.e. the layers with unconnected
    # outputs
    return [layers_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


# Draw the predicted bounding box
def draw_predict(frame, conf, left, top, right, bottom):

    a = '20'
    # Draw a bounding box.
    cv2.rectangle(frame, (left, top), (right, bottom), COLOR_YELLOW, -1)

    text = '{:.2f}'.format(conf)

    # Display the label at the top of the bounding box
    label_size, base_line = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

    top = max(top, label_size[1])
    cv2.putText(frame, text, (left, top - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                COLOR_WHITE, 1)
    if float(text) * 10 > 7.3 or float(text) * 10 < 6:
        a = '20'
    else:
        a = '30'
    cv2.putText(frame, " M, " + a + "s ", (right - 50 , top - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                COLOR_WHITE, 1)
    


def post_process(frame, outs, conf_threshold, nms_threshold, centerPoints, passed, standLineX):
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]

    # Scan through all the bounding boxes output from the network and keep only
    # the ones with high confidence scores. Assign the box's class label as the
    # class with the highest score.
    confidences = []
    boxes = []
    final_boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold:
                center_x = int(detection[0] * frame_width)
                center_y = int(detection[1] * frame_height)
                width = int(detection[2] * frame_width)
                height = int(detection[3] * frame_height)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # Perform non maximum suppression to eliminate redundant
    # overlapping boxes with lower confidences.
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold,
                               nms_threshold)
    
    
    count = 0
    passCount = 0
    # maxindice = 0
    
    # while len(centerPoints) < 40:
    #     centerPoints.append([])


    while len(centerPoints) < len(indices):
        centerPoints.append([])

    for m in indices:
        # jinoo
        count += 1
        
        print("count : ", count) 
        # print("indices type : ", type(indices))

        k = len(indices)
        print("indices length : ", k)
        # print("indices : ", indices)
        m = m[0]
        # print(i)
        # print(type(i), end=' ,')
        # i = len(confidences) -1
        # if maxindice < k:
        #     maxindice = k

        box = boxes[m]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        final_boxes.append(box)
        # print("final_boxes : ", final_boxes)
        left, top, right, bottom = refined_box(left, top, width, height)
        # draw_predict(frame, confidences[i], left, top, left + width,
        #              top + height)
        print("left, top, right, bottom, width, height : ", left, end=' ,') 
        print(top, end=' ,') 
        print(right, end=' ,') 
        print(bottom, end=' ,') 
        print(width, end=' ,') 
        print(height)

        # print("m : ", m)
        # lenCen = len(centerPoints)

        centerX = (left + right) // 2
        centerY = (top + bottom) // 2

        
        if len(centerPoints[count-1]) == 0:
            # if centerX < 1000:
                centerPoints[count-1].append(   (centerX, centerY)   )
            # else:
            #     continue
    

        i = 0
        temp = 0
        nearBox = -1
        minNearStand = 9999

        for number in range(len(centerPoints)):
            
            if len(centerPoints[number]) == 0:
                continue

            temp = abs(centerPoints[number][-1][0] - centerX) + abs(centerPoints[number][-1][1] - centerY)
            
            if temp < minNearStand:
                minNearStand = temp
                nearBox = number

        if minNearStand <400:
            centerPoints[nearBox].append(   (centerX, centerY)   )
        else:
            centerPoints.append([])
            centerPoints[-1].append(   (centerX, centerY)   )

        print(centerPoints)

                    
# 고치는 아이디어 선을 짤짤이로 그리고 좌표위치로 하차를 판별하는게아니라 이동을 가지고
            # print("centerPoints[" + str(i) + "]",centerPoints[i])    
            # print(centerPoints[i])

            


        draw_predict(frame, confidences[m], left, top, right, bottom)


    w = 0
    i = 0
    # drawing whiteline
    for w in range(len(centerPoints)):
        # if len(centerPoints[w]) > 1:
        #     for i in range( len(centerPoints[w])-1 ):
        #         cv2.line(frame, centerPoints[w][i], centerPoints[w][i+1], COLOR_WHITE, 1)
        cv2.line(frame, centerPoints[w][0], centerPoints[w][-1], COLOR_BLUE, 1)

    # counting pass
    passCount = 0
    i=0

    # 선긋기

    for w in range(len(centerPoints)):
        if len(centerPoints[w]) > 1:
            if centerPoints[w][0][0] < standLineX and centerPoints[w][-1][0] > standLineX:
                passCount += 1
                if passed[0] < passCount:
                    passed[0] = passCount
        # if len(centerPoints[w]) > 1:
        #     if centerPoints[w][0][0] > standLineX and centerPoints[w][-1][0] < standLineX:
        #         passCount += 1
        #         if passed[0] < passCount:
        #             passed[0] = passCount
               
                
                    

    # passed.append(passCount)
       
    
    return final_boxes


class FPS:
    def __init__(self):
        # store the start time, end time, and total number of frames
        # that were examined between the start and end intervals
        self._start = None
        self._end = None
        self._num_frames = 0

    def start(self):
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        self._end = datetime.datetime.now()

    def update(self):
        # increment the total number of frames examined during the
        # start and end intervals
        self._num_frames += 1

    def elapsed(self):
        # return the total number of seconds between the start and
        # end interval
        return (self._end - self._start).total_seconds()

    def fps(self):
        # compute the (approximate) frames per second
        return self._num_frames / self.elapsed()

def refined_box(left, top, width, height):
    right = left + width
    bottom = top + height

    original_vert_height = bottom - top
    top = int(top + original_vert_height * 0.15)
    bottom = int(bottom - original_vert_height * 0.05)

    margin = ((bottom - top) - (right - left)) // 2
    left = left - margin if (bottom - top - right + left) % 2 == 0 else left - margin - 1

    right = right + margin

    return left, top, right, bottom
