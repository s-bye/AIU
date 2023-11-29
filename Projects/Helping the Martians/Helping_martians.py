import random

cargo_weight = [300, 250, 163]

while True:
    cargo_location = random.sample(range(1, 8), 3)
    print(f'Current cargo location: {cargo_location}')
    kilometer_marks = []
    for i in range(3):
        kilometer_mark = int(input(f'Enter the kilometer mark for box {i + 1}: '))
        kilometer_marks.append(kilometer_mark)
    total_weight = 0
    cargo_found = True
    for i in range(3):
        if kilometer_marks[i] != cargo_location[i]:
            cargo_found = False
            break
        total_weight += cargo_weight[i]
    if cargo_found and total_weight == 713:
        print('Yes')
        break
    else:
        print('No')
