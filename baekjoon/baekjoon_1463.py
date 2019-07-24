import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def bfs():
    q = deque()
    q.append(t)
    visit[t] = 0
    while q :
        x = q.popleft()

        if x==1:
            print(visit[x])
            return
        for i in range(3):
            if i == 0 and x%3==0:
                nx = x//3
            elif i==1 and x%2==0:
                nx = x//2
            else: nx = x-1

            if nx not in visit:
                visit[nx] = visit[x]+1
                q.append(nx)






t = int(read())
visit = dict()
bfs()