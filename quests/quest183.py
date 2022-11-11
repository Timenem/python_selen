"""
In a string we describe a road. There are cars that move to the right and we denote them with ">" and cars that move to the left and we denote them with "<". There are also cameras that are indicated by: " . ".
A camera takes a photo of a car if it moves to the direction of the camera.

Task
Your task is to write a function such that, for the input string that represents a road as described, returns the total number of photos that were taken by the cameras. The complexity should be strictly O(N) in order to pass all the tests. 
"""

def count_photos(road: str) -> int:
    cam_counter = 0
    forward = road.count('.')
    back = 0
    for i in range(len(road)):
        if road[i] == '<':
            cam_counter += back
        elif road[i] == '>':
            cam_counter += forward
        else:
            forward -= 1
            back += 1
    return cam_counter
