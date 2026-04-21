import cv2
import subprocess

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 30)

gst_out = (
    "appsrc ! videoconvert ! video/x-raw,format=I420 ! "
    "x264enc tune=zerolatency bitrate=2000 speed-preset=ultrafast ! "
    "rtspclientsink location=rtsp://192.168.4.100:8554/drone"
)

out = cv2.VideoWriter(gst_out, cv2.CAP_GSTREAMER, 0, 30, (1920, 1080), True)

print("Streaming at rtsp://192.168.4.100:8554/drone")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)

cap.release()
out.release()
