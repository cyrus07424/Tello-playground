import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
img = cv2.cvtColor(frame_read.frame)
cv2.imwrite("picture.png", img)

tello.land()