# Import Required Packages
from djitellopy import Tello
import time

# Function for flight
def flight(drone: Tello):
    # Take off and hover
    drone.takeoff()
    
    # Flight Actions
    drone.move_up(100)
    drone.rotate_counter_clockwise(360)
    
    # Land after mission completion
    drone.land()