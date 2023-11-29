import random

cargo_location = [3, 5, 6]
cargo_weight = [300, 250, 163]
random.shuffle(cargo_location)
random.shuffle(cargo_weight)
cargo_found = False

while not cargo_found:
    print(f'Current cargo location: {cargo_location}')
    for i in range(3):
        kilometer_mark = int(input(f"Enter the kilometer mark for box {i + 1}: "))
        kilometer_mark.append(kilometer_mark)