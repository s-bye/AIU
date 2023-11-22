import random 
boxes = [231, 235, 247]
distance = 7 
def generate_legs(distances):
    legs = [False] * (distance + 1)
    for distance in distances:
        legs[distance] = True 
    return legs
