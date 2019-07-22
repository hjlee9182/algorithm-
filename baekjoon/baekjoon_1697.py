import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

dx = [1,-1,2]
def bfs():
    q = deque()
    min_num = 10000000000000
    visit[n] = 1
    q.append(n)
    while q:
        x = q.popleft()
        for i in range(3):
            if i == 2 :
                nx = 2*x
            else :
                nx = dx[i]+x

            if nx == t:
                min_num = min(min_num,mat[x]+1)
                mat[nx] = min_num
                continue
            if nx<0 or nx>len(mat)-1:
                continue
            if nx>=0 and nx<=len(mat)-1 and visit[nx]==0:
                visit[nx] = 1
                mat[nx] = mat[x]+1
                q.append(nx)
    print(mat[t])


mat = [0]*100001
visit = [0]*100001

n,t = map(int,read().split())
if n==t :
    print(0)
    sys.exit()
bfs()