import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy

mat = [0 for i in range(10)]

n = int(read())

if n==0:
    print(1)
    exit()

while n!=0:

    a = n%10
    if a==9 or a==6:
        mat[9]+=1
    else:
        mat[a]+=1
    n = n//10


if mat[9]%2==0:
    mat[9] = mat[9]//2
else:
    mat[9] = mat[9]//2+1

print(max(mat))