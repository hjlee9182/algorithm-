import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections

n = int(read())
li = list(map(int,read().split()))

li = set(li)
li = list(li)
li.sort()

print(' '.join(map(str,li)))