month_number = int(input())

if 1 <= month_number <= 12:
    if month_number in [1,3,5,7,8,10,12]:
        days = 31
    elif month_number in [4,6,9,11]:
        days = 30
    else:
        days = 28
    print(days)
else:
    print('0')