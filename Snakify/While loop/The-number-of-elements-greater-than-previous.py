p = int(input())
ans = 0
while p != 0:
    n = int(input())
    if n != 0 and p < n:
        ans += 1
    p = n
print(ans)