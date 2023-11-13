str = input()
f = 'f'
first_f = str.find(f)
last_f = str.rfind(f)

if first_f != -1:
    if first_f == last_f:
        print(first_f)
    else:
        print(first_f, last_f)