# Import Required Packages
from djitellopy import Tello
import time

# Function for specifying a custom flight path
def flight(drone: Tello):
    """
    Controls a DJI Tello drone for a flight from start to finish.

    Args:
         drone: Tello (djiteleopy) object that specifies actions to be taken on a DJI Tello drone over WiFi and offers data streaming capabilities.
         
    Returns:
         None
    """
    # [Do Not Edit] Take off and hover
    drone.takeoff()
    
    # [Edit this part to specify a custom flight path] Flight Actions
    drone.move_up(100)
    drone.rotate_counter_clockwise(360)
    
    # [Do Not Edit] Land after mission completion
    drone.land()
    