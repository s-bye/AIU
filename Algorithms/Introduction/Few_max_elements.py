ages = [10, 6, 15, 93, 42, 7, 32]
maxAge = 0
for i in range(len(ages)):
    maxAge = max(maxAge, ages[i])

maxAge2 = 0

for i in range(len(ages)):
    if ages[i] < maxAge:
        maxAge2 = max(maxAge2, ages[i])

print(maxAge)
print(maxAge2)
