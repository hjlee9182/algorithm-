import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

dp = [0]*11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
t= int(read())
while t>0 :
    m = int(read())
    print(dp[m])
    t-=1