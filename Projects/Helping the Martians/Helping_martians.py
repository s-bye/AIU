import random

def generate_cargo_location(): # Function, that generates a random location of cargoes.
    return random.sample(range(1, 8), 3)

def calculate_total_weight(cargo_weight, kilometer_marks, cargo_location): # Function, that calculates the total weight of the cargo.
    total_weight = sum(cargo_weight[i] for i in range(3) if kilometer_marks[i] == cargo_location[i])
    return total_weight

def check_cargo_location(kilometer_marks, cargo_location, cargo_weight): # Function, that checks if the cargo location is correct and calculates the total weight of the cargo.
    for i in range(3):
        if kilometer_marks[i] != cargo_location[i]:
            return False
    
    total_weight = 0
    for i in range(3):
        if kilometer_marks[i] == cargo_location[i]:
            total_weight += cargo_weight[i]
    
    return total_weight == 713

def validate_input(digit): # Function, that ensuring input data and ensuring it's a number between 1-7.
    return 0 < digit < 8

def main():
    cargo_weight = [300, 250, 163] # Cargoes weight
    
    print("Welcome! You need to help the Martians, and to do that, you need to find the cargoes.")
    print("You'll be asked to enter kilometer marks from 1 to 7, where the cargo might be buried.")
    
    while True:
        cargo_location = generate_cargo_location()
        print(f'Current cargoes location: {cargo_location}')  # Shows current location of cargoes, helps to check the program, if you want to find it without it's help, remove this line.
        kilometer_marks = []
        
        for i in range(3):
            while True:
                kilometer_mark = int(input(f'Enter the kilometer mark for box {i + 1}: ')) # Input from user.
                if validate_input(kilometer_mark):
                    kilometer_marks.append(kilometer_mark)
                    break
                else:
                    print('Please write a kilometer mark from 1 to 7.') 
        
        total_weight = calculate_total_weight(cargo_weight, kilometer_marks, cargo_location)
        cargo_found = check_cargo_location(kilometer_marks, cargo_location, cargo_weight)
        
        if cargo_found and total_weight == 713:
            print('Congratulations! You found all the cargoes!') # Cargoes was found, success message
            break
        else:
            print('Unfortunately, the cargoes were not found. Cargoes have changed their location, please enter new kilometr marks.') # Cargoes wasn't found, failure message

if __name__ == "__main__":
    main()
