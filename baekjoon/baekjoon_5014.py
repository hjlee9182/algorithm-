import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

f,s,g,u,d = map(int,read().split())
q = deque()

s-=1
g-=1
mat = [0]*f
visit = [0]*f
q.append(s)
if s==g :
    print(0)
    sys.exit()
min_num = 10000000000000000000000000000
while q:
    x = q.popleft()
    visit[x] = 1
    for i in range(2):

        if i ==0 :
            nx = x + u
        else:
            nx = x - d
        if nx == g:
            min_num = min(min_num, mat[x] + 1)
            mat[nx] = min_num
            continue
        if 0<=nx and nx<f and visit[nx]==0:
            mat[nx] = mat[x] + 1
            visit[nx]= 1
            q.append(nx)


if mat[g] == 0 :
    print("use the stairs")
else :
    print(min_num)