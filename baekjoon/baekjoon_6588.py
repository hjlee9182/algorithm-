import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections
import heapq

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return sieve
    #return [i for i in range(2, n) if sieve[i] == True]


li = prime_list(1000000)

while True:
    n = int(read())
    if n==0:
        break
    else:
        flag = 0
        for i in range(3,n):
            if li[i]==True and li[n-i]==True:
                print(f'{n} = {i} + {n-i}')
                flag = 1
                break
        if flag==0:
            print('Goldbach\'s conjecture is wrong.')