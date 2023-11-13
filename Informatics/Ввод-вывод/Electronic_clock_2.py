n = int(input())
h = n // 3600 % 24
n = n % 3600
m = n // 60
n = n % 60
s = n
print(f'{h}:{m:02d}:{s:02d}')
