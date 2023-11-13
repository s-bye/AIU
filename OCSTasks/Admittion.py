import os

english_levels = {
    1: "Beginner",
    2: "Elementary",
    3: "Pre-Intermediate",
    4: "Intermediate",
    5: "Upper-Intermediate",
    6: "Advanced",
}

discounts = {
    "140-155": 0.05,
    "156-174": 0.10,
    "175-199": 0.25,
    "200-209": 0.50,
    "210-218": 0.75,
    "219-240": 1,
}

def get_applicant_data():
    lastname = input("Enter your last name: ")
    firstname = input("Enter your first name: ")
    ort = int(input("Enter your ORT score: "))
    school_certificate = bool(int(input("Do you have a school education certificate? (0 for 'No', 1 for 'Yes'): ")))
    english_level = int(input("Choose your English proficiency level(1-6):\n1: A1\n2: A2\n3: B1\n4: B2\n5: C1\n6: C2\n"))
    return lastname, firstname, ort, school_certificate, english_level

def is_admitted(ort, school_certificate, english_level):
    if not school_certificate:
        print("You cannot be admitted to Ala-Too University without a school education certificate.")
        return False
    elif ort < 110:
        print("Your ORT score is below the required minimum (110). You cannot be admitted.")
        return False
    elif english_level < 4:
        print("Your English proficiency level is too low for admission. You may need to take a preparatory English course.")
        return False
    return True

def calculate_tuition_fee(specialty):
    tuition_fee = {
        "Computer Engineering": 2500,
        "Artificial Intelligence": 2200,
        "Psychology": 1900,
        "Journalism": 1700,
        "International Relations": 2200,
        "Law": 1800,
        "Management": 2200,
        "Medicine": 3300,
    }
    return tuition_fee.get(specialty, 0)

def calculate_discount(ort):
    for score_range, discount_percentage in discounts.items():
        start, end = map(int, score_range.split('-'))
        if start <= ort <= end:
            return discount_percentage
    return 0

def final_message(lastname, firstname, specialty, tuition_fee_with_discount, discount_percentage):
    print(f"Dear {lastname} {firstname}, we congratulate you! You have been admitted to the {specialty} program at Ala-Too International University.")
    if discount_percentage > 0:
        print(f"The cost of your tuition with a {int(discount_percentage * 100)}% discount will be ${tuition_fee_with_discount:.0f} per year.")
    else:
        print(f"The cost of your tuition will be ${tuition_fee_with_discount:.0f} per year.")

if __name__ == "__main__":
    os.system('cls')
    lastname, firstname, ort, school_certificate, english_level = get_applicant_data()
    if not is_admitted(ort, school_certificate, english_level):
        exit()
    os.system('cls')
    print('''
        There is available specialties in Ala-Too university:
        Computer Engineering: 2500$
        Artificial Intelligence: 2200$
        Psychology: 1900$
        Journalism: 1700$
        International Relations: 2200$
        Law: 1800$
        Management: 2200$
        Medicine: 3300$
    ''')
    desired_specialty = input("Select your desired specialty: ")
    tuition_fee = calculate_tuition_fee(desired_specialty)
    discount = calculate_discount(ort)
    tuition_fee_with_discount = tuition_fee - (tuition_fee * discount)
    os.system('cls')
    final_message(lastname, firstname, desired_specialty, tuition_fee_with_discount, discount)