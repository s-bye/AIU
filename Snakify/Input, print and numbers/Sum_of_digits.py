num = int(input())
f_digit = num // 100
s_digit = num // 10 % 10
t_digit = num % 10
print(f_digit + s_digit + t_digit)