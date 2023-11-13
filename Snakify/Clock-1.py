h = int(input("Enter hours (0-11): "))
m = int(input("Enter minutes (0-59): "))
s = int(input("Enter seconds (0-59): "))

hour_angle = 30 * (h % 12) + 0.5 * m + (1/120) * s

print(hour_angle)