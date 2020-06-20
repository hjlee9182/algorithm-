import sys

read = lambda : sys.stdin.readline().strip()
from collections import deque

n = int(read())
mat = []
for i in range(n):
    mat.append(list(map(int,read().split())))
dp = [0 for i in range(n+1)]

for i in range(n):
    if i+mat[i][0]<=n:
        dp[i+mat[i][0]] = max(dp[i+mat[i][0]],max(dp[:i+1])+mat[i][1])
print(max(dp))
