# Import Required Packages
from djitellopy import Tello
from threading import Thread
from video_test_flight import flight
import cv2
import time
import os

# Helper Functions for Data Collection
def take_individual_picture(drone) -> None:
    """
    Uses the camera onboard the DJI Tello Drone to take a singular image. Image is captured via OpenCV interfacing with the Drone stream, and downlinked to the DroneFormer/Images folder.

    Args:
        drone: Tello (djiteleopy) object that specifies actions to be taken on a DJI Tello drone over WiFi and offers data streaming capabilities.
        
    Returns:
        None
    """
    drone.streamon()
    frame_read = drone.get_frame_read()
    image_directory = os.path.join(os.path.abspath(os.path.join('..')), "Images")
    title = "single_image_" + str(time.time()) + ".jpg"
    current_frame = frame_read.frame
    cv2.imwrite(os.path.join(image_directory, title), current_frame)
    

def stream_frames(drone, save=False):
    """
    Creates and displays a live stream of images from the DJI Tello Drone using OpenCV, frame by frame.

    Args:
        drone: Tello (djiteleopy) object that specifies actions to be taken on a DJI Tello drone over WiFi and offers data streaming capabilities.
        save (bool, optional): Indicator that specifies whether or not to save images locally. Defaults to False (stream window will pop up).
        
    Returns:
        None
    """
    drone.streamon()
    while True:
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        if save:
            title = "image_" +str(time.time()) + ".jpg"
            cv2.imwrite("./"+title, img)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        

def record_streamed_frames(drone):
    """
    Records a live stream of images (frame by frame) from the DJI Tello Drone using OpenCV and saves the frames as an MP4 video file locally.

    Args:
        drone: Tello (djiteleopy) object that specifies actions to be taken on a DJI Tello drone over WiFi and offers data streaming capabilities.
        
    Returns:
        None
    """
    drone.streamon()
    frame = drone.get_frame_read().frame
    height, width, _ = frame.shape
    video = cv2.VideoWriter( "output_video.mp4",cv2.VideoWriter_fourcc(*"MP4V"),30,(width,height))

    start = time.time()
    while (time.time() - start) < 60:
        frame = drone.get_frame_read().frame
        video.write(frame)
        time.sleep(1/30)
    
    video.release()
    
    
def stream_video():
    """
    Legacy function to stream video directly from the DJI Tello Drone and save the resulting video MP4 file simultaneously to the local directory.
    
    Args:
        None
        
    Returns:
        None
    
    """
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
            cv2.VideoWriter_fourcc(*"mp4v"), # Video Codec, can use "XVID" or "X264" as alternatives
            30, # Frame Rate
            (width, height) # Video Resolution
        )

        while keepRecording == True:
            video.write(frame_read.frame)
            time.sleep(float(1/fps)) # 30 FPS
        
        video.release()
        
    recorder = Thread(target = record_video)
    recorder.start()
    
    # Run this function to get the actions for the flight
    flight(drone)
        
    keepRecording = False
    recorder.join()
