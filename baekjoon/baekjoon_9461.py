import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

dp = [0]*101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9
for i in range(11,101):
    dp[i] = dp[i-2]+dp[i-3]

t = int(read())
while t>0:
    m = int(read())
    print(dp[m])
    t-=1