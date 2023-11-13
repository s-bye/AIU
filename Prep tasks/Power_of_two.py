n = int(input())
powers_of_two = []
power_of_two = 1

while power_of_two <= n:
    powers_of_two.append(power_of_two)
    power_of_two *= 2

print(powers_of_two)