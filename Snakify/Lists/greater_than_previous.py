list = input().split()
list = [int(x) for x in list]
greater = []
for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        print(list[i])