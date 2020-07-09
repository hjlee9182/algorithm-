import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy
import collections

n = int(read())
d = dict()
for _ in range(n):
    name,inout = read().split()
    if inout=='enter':
        d[name] = 'enter'
    else:
        d.pop(name)

re = sorted(d.keys(),reverse=True)
for keys in re:
    print(keys)