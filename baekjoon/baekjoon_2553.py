import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy
import collections

n = int(read())
result = 1
for _ in range(1,n+1):
    result = result*_

result= str(result)
for i in range(len(result)-1,-1,-1):
    if result[i]!='0':
        print(result[i])
        break