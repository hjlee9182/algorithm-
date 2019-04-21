import math

n,m = input().split()

n = int(n)
m = int(m)

sum = math.factorial(n)//math.factorial(n-m)//math.factorial(m)

print(sum)
