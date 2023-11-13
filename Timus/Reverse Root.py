import sys
nums = []
for line in sys.stdin:
    for word in line.split():
        nums.append(float(word))
nums=nums[::-1]
for num in nums:
    print("%.4f" % (num)**0.5)