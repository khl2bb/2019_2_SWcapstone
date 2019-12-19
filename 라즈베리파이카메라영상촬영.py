from picamera import PiCamera
from time import sleep

camera = PiCamera()



#동영상 녹화 시작
camera.start_recording(output = 'video.h264')

#10초동안 녹화하기
camera.wait_recording(10)

#동영상 녹화 종료
camera.stop_recording()

