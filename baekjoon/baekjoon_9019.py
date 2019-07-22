import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def fun_l(a):
    return (a%1000)*10+(a//1000)

def fun_r(a):
    return (a//10)+(a%10)*1000

def bfs():
    min_num = 100000000000000
    while q:
        x = q.popleft()
        visit[x] = 1
        for i in range(4):
            if dx[i] =='D':
                nx = 2*x
                if nx>9999 :
                    nx = nx%10000
            if dx[i] == 'S':
                if x == 0 :
                    nx = 9999
                else:
                    nx = x-1
            if dx[i] == 'L':
                nx = fun_l(x)
            if dx[i] == 'R':
                nx = fun_r(x)

            if nx ==t:
                print(mat[x]+dx[i])
                return

            if nx<0 or nx>=10000:
                continue
            if mat[nx] =='' and visit[nx]==0:
                mat[nx] = mat[x]+dx[i]
                visit[nx] = 1
                q.append(nx)
    print(mat[t])


tar = int(read())
dx = ['D','S','L','R']
while tar>0:
    s,t = map(int,read().split())
    q = deque()
    q.append(s)
    mat = ['']*10000
    visit = [0]*10000
    bfs()
    tar-=1