prompt_template="""
You are writing code to control a drone.
Here is a list of commands:
    drone.move_left(X)  - move the drone left by X centimeters, where X is between 20 and 50
    drone.move_right(X) - move the drone right by X centimeters, where X is between 20 and 50
    drone.move_forward(X) - move the drone forward by X centimeters, where X is between 20 and 50
    drone.move_back(X) - move the drone back by X centimeters, where X is between 20 and 50
    drone.takeoff() - lift off the drone
    drone.land() - land the drone
    drone.rotate_clockwise(X) - rotate the drone clockwise by X degrees, where X is between 1 and 360
    drone.rotate_counter_clockwise(X) - rotate the drone counter-clockwise by X degrees, where X is between 1 and 360
    object_detect(X) - takes in the name of an object X, and returns True or False depending on whether the object is in the frame. valid values for X are [bottle, person, chair]

Write the code needed for an algorithm to $objective
You need to start by taking off with the drone.takeoff() command and end by landing with the drone.land() command.
Please insert helpful print statements to document the progress towards the objective.
"""