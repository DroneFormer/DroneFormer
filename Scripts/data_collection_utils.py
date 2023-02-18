# Import Required Packages
from djitellopy import Tello
from threading import Thread
from video_test_flight import flight
import cv2
import time
import os

# Helper Functions for Data Collectin
def take_individual_picture(drone):
    drone.streamon()
    frame_read = drone.get_frame_read()
    image_directory = os.path.join(os.path.abspath(os.path.join('..')), "Images")
    title = "image_" + str(time.time()) + ".jpg"
    current_frame = frame_read.frame
    cv2.imwrite(os.path.join(image_directory, title), current_frame)
    
    
def stream_video():
    # Configure Drone
    drone = Tello()
    drone.connect()
    drone.streamon()
    frame_read = drone.get_frame_read()
    
    # Static Vars
    keepRecording = True
    video_directory = os.path.join(os.path.abspath(os.path.join('..')), "Videos")
    title = os.path.join(video_directory, "test_video.mp4")
    fps = 30
    
    # Record Video
    def record_video():
        height, width, _ = frame_read.frame.shape
        video = cv2.VideoWrite(
            title,
            cv2.VideoWriter_fourcc(*"mp4v"), # Video Codec, can use "mp4v" or "X264" as alternatives
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
    flight(drone)
        
    keepRecording = False
    recorder.join()