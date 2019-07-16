import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def bfs():
    q = deque()
    q.append(src)
    while q:
        now = q.popleft()
        if now == target :
            return dist[now]
        for i in mat[now]:
            if dist[i] == 0:
                q.append(i)
                dist[i] = dist[now]+1
    return -1


num = int(read())
src,target = map(int,read().split())
m = int(read())
mat = [[] for _ in range(num+1)]
dist =[0 for _ in range(num+1)]

for _ in range(m):
    a, b = map(int,read().split())
    mat[a].append(b)
    mat[b].append(a)

print(bfs())