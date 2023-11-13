mass = []
x = []
y = []

for i in range(4):
    mass.append([int(input('Write x ')), int(input('Write y '))])

for i in mass:
    x.append(i[0])
    y.append(i[1])
2
print(x)
print(y)

reskx = x[0] * y[1] + x[1] * y[2] + x[2] * y[3] + x[3] * y[0]
resky = x[1] * y[0] + x[2] * y[1] + x[3] * y[2] + x[0] * y[3]
resxy = abs(reskx - resky) / 2

print(resxy)