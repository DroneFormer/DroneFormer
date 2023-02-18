# Import Required Packages
from djitellopy import Tello

# Initialize an object of DJI Tello Class
drone = Tello()

# Connect to the Tello Drone
drone.connect()

# Take off and hover
drone.takeoff()




# Land after mission completion
drone.land()