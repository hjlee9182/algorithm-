import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections



m = int(read())
a = list(map(int,read().split()))
b = list(map(int,read().split()))

a.sort(reverse = True)
b.sort()

answer = 0
for i in range(m):
    answer +=a[i]*b[i]
print(answer)
