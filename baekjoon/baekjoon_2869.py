import math
a,b,c = map(int,input().split())
c = c-a
k = math.ceil(c/(a-b))

print(k+1)