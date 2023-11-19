import time
while True:
    login = input()
    if login.isdigit():
        break
    else:
        print("Invalid username")
while True:
    password = input()
    if password.isdigit():
        break
    else:
        print("Invalid password")
attempts = 0
while True:
    true_login = '230121033'
    true_password = '12345678'
    if login == true_login and password == true_password:
        print('Access granted')
        break
    else:
        attempts += 1 
        if attempts => 3:
            print('Too many failed attempts, please try again after 5 seconds')
            time.sleep(5)
            attempts = 0