import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

n = int(read())

dp = [0]*91
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])