def isDifferent(n):
    return len(set(str(n))) == len(str(n))
def findNext(n):
    n += 1
    while not isDifferent(n):
        n += 1
    return n
n = int(input())
print(findNext(n))
 