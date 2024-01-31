user = {}

user["Name"] = input("What is the user's name? ")
user["Age"] = int(input("What is the user's age? "))
user["Country"] = input("What is the user's country of birth? ")
user["Known for"] = input("What is the user known for? ")

for key, value in user.items():
    print(f"{key} : {value}")
