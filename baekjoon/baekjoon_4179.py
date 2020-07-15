import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    global people,fire

    visit = [[0 for i in range(m)]for j in range(n)]
    time = 1
    fq = collections.deque()
    pq = collections.deque()
    for i in range(len(fire)):
        fq.append(fire[i])
    for i in range(len(people)):
        pq.append(people[i])
    visit[people[0][0]][people[0][1]] = 1

    while True:

        lenfq = len(fq)
        for _ in range(lenfq):
            x,y = fq.popleft()

            for i in range(4):
                x_ = x+dx[i]
                y_ = y+dy[i]

                if 0<=x_<n and 0<=y_<m:
                    if mat[x_][y_]=='.' or mat[x_][y_]=='J':
                        fq.append((x_,y_))
                        mat[x_][y_] = 'F'

        lenpq = len(pq)
        if lenpq==0:
            break
        for _ in range(lenpq):
            x, y = pq.popleft()

            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]

                if 0 <= x_ < n and 0 <= y_ < m:
                    if (mat[x_][y_] == '.') and visit[x_][y_]==0:
                        pq.append((x_, y_))
                        visit[x_][y_] = 1
                else:
                    return time
        time+=1

    return -1





n,m = map(int,read().split())

mat = []
people = []
fire = []
for _ in range(n):
    li = list(read())
    mat.append(li)
    for i in range(m):
        if mat[_][i]=='J':
            people.append((_,i))
        elif mat[_][i]=='F':
            fire.append((_,i))
t = bfs()
if t==-1:
    print("IMPOSSIBLE")
else:
    print(t)
