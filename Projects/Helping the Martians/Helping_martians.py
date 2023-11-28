import random 

cargo_weight = 713
num_boxes = 3
box_locations = [0, 0, 0]
cargo_found = False

while not cargo_found:
    kilometer_marks = []
    for i in range(num_boxes):
        for i in range(num_boxes):
            kilometer_mark = int(input(f'Enter the kilometer mark for box {i + 1}: '))
            kilometer_marks.append(kilometer_mark)
            
    total_weight = 0
    
    for i, kilometer_mark in enumerate(kilometer_marks):
        if box_locations[i] == kilometer_mark:
            total_weight += cargo_weight
        else:
            box_locations[i] = random.randint(0, 7)
            
    if total_weight == cargo_weight:
        cargo_found  = True
        print("All the cargo has been found!")
    else:
        print("The cargo has not been found. Please enter the kilometer marks again.")        