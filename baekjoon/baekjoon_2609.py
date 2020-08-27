import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections
gcd = lambda a, b: gcd(b, a % b) if a % b else b

m,n = map(int,read().split())

g = gcd(n,m)
print(g)
print(m*n//g)