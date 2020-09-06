import numpy as np
import sys
import cv2
import os

argLength = len(sys. argv)
if(argLength != 2):
    print('Invalid number of arguments.')
    print('Input format: python convert.py <VideoFileName>')
    sys.exit()

file_name = sys.argv[1]

valid_types = ('.mp4', '.wav', '.avi', '.mov')

file_type = os.path.splitext(file_name)[1]
if(file_type.lower() not in valid_types):
    print('File format not supported.')
    print('Supported formats: ', valid_types)
    sys.exit()

if not os.path.isfile(file_name):
    print('Video file not found.')
    sys.exit()

cap = cv2.VideoCapture(file_name)

ret, frame = cap.read()
if not ret:
    print('Video file not found.')
    sys.exit()

fps = cap.get(cv2.CAP_PROP_FPS)

FrameSize=(frame.shape[1], frame.shape[0])

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('video_output.mp4', fourcc, fps, FrameSize, 0)

length = cap.get(cv2.CAP_PROP_FRAME_COUNT)
ani = "|///———\\\||"
idx = 0
while True:
    ret, frame = cap.read()

    if ret == True:
        print('', ani[idx%len(ani)], 'Converting video:', int(idx*100/length)+1, '\b% complete', end="\r")
        idx += 1
        grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(grayed_frame)
    else:
        print('\bVideo converted to grayscale successfully.     ')
        break

cap.release()
out.release()
cv2.destroyAllWindows()