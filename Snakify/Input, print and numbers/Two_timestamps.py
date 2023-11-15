h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

total_sec1 = h1 * 3600 + m1 * 60 + s1
total_sec2 = h2 * 3600 + m2 * 60 + s2

time_dif = total_sec2 - total_sec1

print(time_dif)