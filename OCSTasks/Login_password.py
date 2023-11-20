import time
def data_input():
    # Inputs user login and password. 
    login = input('Login: ')
    password = input('Password: ')
    return login, password

def validating_data(login, password):
    # Validate login credentials. 
    true_login = '230121033'
    true_password = '12345678'
    # Check if the entered credentials match the correct ones
    if login == true_login and password == true_password:
        return True
    else:
        return False

attempts = 0 # Initialize the counter for incorrect attempts
attempts_left = 3 # Set the maximum number of allowed incorrect attempts

while True:
    login, password = data_input()
    if validating_data(login, password):
        print('Access granted. Welcome to the system!')
        break # Exit the loop upon successful login
    else:
        attempts += 1
        attempts_left -= 1  
        print(f'Invalid login or password, please recheck your login and password and try again. Attempts left: {attempts_left}')
    if attempts == 3:
        print('Too many incorrect attempts. Please try again after 5 seconds')
        time.sleep(5) # Wait for 5 seconds before allowing further attempts
        print('You can now try again.')
        attempts = 0
        attempts_left = 3
