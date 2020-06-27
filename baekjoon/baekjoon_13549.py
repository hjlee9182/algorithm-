import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy

dx = [-1,1]
def bfs():
    q = deque()
    q.append((n,0))
    visit = [9999999999999 for i in range(100001)]
    visit[n] = 0
    result = 9999999999999
    while len(q)>0:
        number,time = q.popleft()

        for i in range(2,-1,-1):
            if i==2:
                x = number*2
            else:
                x = dx[i]+number
            if 0<=x<=100000:

                if x==k:
                    if i==2:
                        visit[x] = min(visit[x], time)
                    else:
                        visit[x] = min(visit[x],time+1)
                if visit[x]==9999999999999:
                    if i==2:
                        q.appendleft((x, time))
                        visit[x] = time
                    else:
                        q.append((x,time+1))
                        visit[x] = time+1
    print(visit[k])

n,k = map(int,read().split())
bfs()