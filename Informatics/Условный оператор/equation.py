a = int(input())
b = int(input())
if a != b:
    if b%a == 0:
        print(-b//a)
    else:
        print('NO')
    if b == 0:
        print('INF')
else:
    print('-1')