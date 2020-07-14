import sys
read = lambda :sys.stdin.readline().strip()
import itertools

def dfs(now,number):
    global m

    if number == m:
        print(' '.join(map(str,now)))
        return
    else:
        for i in range(now[-1],n+1):
            now.append(i)
            dfs(now,number+1)
            now.pop(-1)

n,m = map(int,read().split())
mat = [i for i in range(1,n+1)]

for i in range(1,n+1):
    dfs([i],1)