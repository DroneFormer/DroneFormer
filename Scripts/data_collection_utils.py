# Import Required Packages
from djitellopy import Tello
from threading import Thread
from video_test_flight import flight
import cv2
import time

# Helper Functions for Data Collectin
def take_individual_picture(drone):
    drone.streamon()
    frame_read = drone.get_frame_read()
    title = "image_" + str(time.time()) + ".jpg"
    current_frame = frame_read.frame
    cv2.imwrite(title, current_frame)
    
    
def stream_video():
    # Configure Drone
    drone = Tello()
    drone.connect()
    drone.streamon()
    frame_read = drone.get_frame_read()
    
    # Static Vars
    keepRecording = True
    title = "test_video.avi"
    fps = 30
    
    # Record Video
    def record_video():
        height, width, _ = frame_read.frame.shape
        video = cv2.VideoWrite(
            title,
            cv2.VideoWriter_fourcc(*"XVID"), # Video Codec, can use "mp4v" or "X264" as alternatives
            30, # Frame Rate
            (width, height) # Video Resolution
        )

        while keepRecording == True:
            video.write(frame_read.frame)
            time.sleep(1/fps) # 30 FPS
        
        video.release()
        
    recorder = Thread(target = record_video)
    recorder.start()
    
    # Run this function to get the actions for the flight
    flight()
        
    keepRecording = False
    recorder.join()
