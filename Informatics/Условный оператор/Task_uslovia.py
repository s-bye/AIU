a = int(input())
b = int(input())
c = int(input())
d = int(input())

total_price = a * 100 + b
total_paid = c * 100 + d

change = total_paid - total_price

e = change // 100
f = change % 100

print(e, f)