import math
n = int(input())
k = int(input())
div_apples = math.floor(k/n)
in_basket = k % n 
print(div_apples)
print(in_basket)