import collections
import sys
read = lambda : sys.stdin.readline().strip()
import itertools

dx = [0,0,1,-1]
dy = [1,-1,0,0]
mat = []
puyo = []
for i in range(12):
    li = read()
    mat.append(list(li))
    for j in range(6):
        if mat[i][j]!='.':
            puyo.append((i,j))
puyo.reverse()
result = 0

while True:

    flag = 0
    map1 = [[0 for i in range(6)]for j in range(12)]
    visit = [0 for i in range(6)]
    every = []
    for x,y in puyo:

        if map1[x][y]==1 or mat[x][y]=='.':
            continue


        check = []
        q = collections.deque()

        if mat[x][y]!='.':

            c = mat[x][y]
            check.append((x,y))
            q.append((x,y))
            visit[y] += 1
            map1[x][y] = 1

            while len(q)>0:

                x1,y1 = q.popleft()
                for i in range(4):
                    x_ = x1+dx[i]
                    y_ = y1+dy[i]
                    if 0<=x_<12 and 0<=y_<6:
                        if mat[x_][y_]==c and map1[x_][y_]==0:
                            check.append((x_,y_))
                            q.append((x_,y_))
                            map1[x_][y_] = 1
                            visit[y_] +=1
            if len(check)>=4:
                every.extend(check)
                flag = 1

            else:
                for x1,y1 in check:
                    map1[x1][y1] = 0
                    visit[y1]-=1


    if flag == 0:
        break
    else:
        for x,y in every:
            mat[x][y] = '.'
        result+=1
        for i in range(len(visit)):
            if visit[i] > 0:
                for k in range(11,-1,-1):
                    if mat[k][i]=='.':
                        for j in range(k-1,-1,-1):
                            if mat[j][i]!='.':
                                mat[k][i] = mat[j][i]
                                mat[j][i] = '.'
                                break



print(result)




