import collections
import sys
read = lambda : sys.stdin.readline().strip()
import itertools

def part(i):
    visited[i] = 1
    li = mat[i]
    for j in range(len(li)):
        if home[li[j]]==-1:
            home[li[j]] = i

            return True
        else:
            t = home[li[j]]
            if visited[t]==0 and part(t):
                home[li[j]] = i
                return True
    return False


n,m = map(int,read().split())

mat = []
home = [ -1 for i  in range(m)]
visit = [0 for i in range(n)]
for i in range(n):
    li = list(map(int,read().split()))
    for j in range(len(li)):
        li[j] = li[j]-1
    mat.append(li[1:])
result = 0
for i in range(n):
    visited =[ 0 for i in range(n)]
    if part(i):
        result+=1
print(result)

