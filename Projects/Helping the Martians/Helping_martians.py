import random

def generate_cargo_location():
    return random.sample(range(1, 8), 3)

def calculate_total_weight(cargo_weight, kilometer_marks, cargo_location):
    total_weight = sum(cargo_weight[i] for i in range(3) if kilometer_marks[i] == cargo_location[i])
    return total_weight

def check_cargo_location(kilometer_marks, cargo_location, cargo_weight):
    for i in range(3):
        if kilometer_marks[i] != cargo_location[i]:
            return False
    
    total_weight = 0
    for i in range(3):
        if kilometer_marks[i] == cargo_location[i]:
            total_weight += cargo_weight[i]
    
    return total_weight == 713

def validate_input(digit):
    return 0 < digit < 8

def main():
    cargo_weight = [300, 250, 163]

    while True:
        cargo_location = generate_cargo_location()
        print(f'Current cargo location: {cargo_location}')
        kilometer_marks = []
        
        for i in range(3):
            while True:
                kilometer_mark = int(input(f'Enter the kilometer mark for box {i + 1}: '))
                if validate_input(kilometer_mark):
                    kilometer_marks.append(kilometer_mark)
                    break
                else:
                    print('1 to 7')
        
        total_weight = calculate_total_weight(cargo_weight, kilometer_marks, cargo_location)
        cargo_found = check_cargo_location(kilometer_marks, cargo_location, cargo_weight)
        
        if cargo_found and total_weight == 713:
            print('Yes')
            break
        else:
            print('No')

if __name__ == "__main__":
    main()
