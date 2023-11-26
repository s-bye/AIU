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
            