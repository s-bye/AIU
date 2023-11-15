n = int(input())
div = 2 
while div <= n:
    if n % div == 0:
        break 
    div += 1
print(div)