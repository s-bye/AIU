import time
def data_input():
    login = input()
    password = input()
    return login, password

def validating_data(login, password):
    true_login = '230121033'
    true_password = '12345678'
    if login == true_login and password == true_password:
        return True
    else:
        return False

attempts = 0
attempts_left = 3

while True:
    login, password = data_input()
    if validating_data(login, password):
        print('Access granted')
        break
    else:
        attempts += 1
        attempts_left -= 1  
        print(f'Invalid login or password, please recheck your login and password and try again. Attempts left: {attempts_left}')
    if attempts == 3:
        print('Too many incorrect attempts. Please try again after 5 seconds')
        time.sleep(5)
        print('Now you can try again!')
        attempts = 0
        attempts_left = 3
