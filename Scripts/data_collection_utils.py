# Import Required Packages
from djitellopy import Tello
import cv2
import time


# Helper Functions for Data Collectin
def take_picture(drone):
    drone.streamon()
    frame_read = drone.get_frame_read()
    title = "image_" + str(time.time()) + ".jpg"
    current_frame = frame_read.frame
    cv2.imwrite(title, current_frame)
    
    
def stream_video(drone):
    


# Initialize an object of DJI Tello Class
drone = Tello()

# Connect to the Tello Drone
drone.connect()

# Take off and hover
drone.takeoff()




# Land after mission completion
drone.land()
