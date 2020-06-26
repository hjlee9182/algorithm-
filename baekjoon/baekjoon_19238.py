import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def check_distance(sx,sy,target):
    global mat

    visit = copy.deepcopy(mat)
    q = deque()
    q.append((sx,sy))

    while len(q)>0:
        x,y = q.popleft()

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0<=x_<n and 0<=y_<n:
                if visit[x_][y_]==0 and not(sx==x_ and sy==y_):
                    visit[x_][y_] = visit[x][y]+1
                    q.append((x_,y_))
    # for i in range(n):
    #     print(visit[i])
    t_s = -1
    t_x = -1
    t_y = -1
    t_d = 33333333
    for i,v in enumerate(target):
        if visit[v[0]][v[1]]==0 and (v[0]!=sx or v[1]!=sy):
            continue
        if visit[v[0]][v[1]]<t_d:
            t_d = visit[v[0]][v[1]]
            t_s,t_x,t_y = i,v[0],v[1]
        elif visit[v[0]][v[1]] == t_d:
            if v[0]<t_x:
                t_d = visit[v[0]][v[1]]
                t_s, t_x, t_y = i, v[0], v[1]
            elif v[0]==t_x:
                if v[1]<t_y:
                    t_d = visit[v[0]][v[1]]
                    t_s, t_x, t_y = i, v[0], v[1]

    return t_s,t_d





n,m,e = map(int,read().split())
mat = []
people = []
for i in range(n):
    li = list(map(int,read().split()))
    mat.append(li)
    for j in range(n):
        if mat[i][j]==1:
            mat[i][j] = -1


cx,cy = map(int,read().split())
cx,cy = cx-1,cy-1

for _ in range(m):
    x,y,z,t = map(int,read().split())
    people.append([x-1,y-1,z-1,t-1])

while True:
    if len(people)==0:
        print(e)
        break

    t_p,td = check_distance(cx,cy,people)
    if t_p==-1:
        print(-1)
        break
    #print(people[t_p],td)
    e-= td
    #print("people e",e)
    cx,cy = people[t_p][0],people[t_p][1]

    t,td = check_distance(cx,cy,[[people[t_p][2],people[t_p][3]]])

    if t==-1:
        print(-1)
        break

    cx,cy = people[t_p][2],people[t_p][3]
    e-= td
    #print("e -",e,td)
    if e<0:
        print(-1)
        break
    else:
        people.remove(people[t_p])

    e+=td*2
    #print("e +",e)

