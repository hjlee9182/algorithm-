# BFS 사용
# 높이가 추가 된거 외에는 기본 BFS랑 풀이 동일

from collections import deque
import sys
def all():
    for z in range(h):
        for i in range(n):
            for j in range(m):
                if mat[z][i][j] == 0:
                    return False
    return True

dz = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]

m,n,h = map(int, input().split())

check = dict()
q = deque()
mat = []

for _ in range(h):
    lis = []
    for i in range(n):
        li = list(map(int, input().split()))
        for j in range(m):
            if li[j] == 1:
                q.append((_,i,j))
                check[(_,i,j)] = 1
        lis.append(li)
    mat.append(lis)

answer = 0
if all():
    print(answer)
    sys.exit()

while len(q) > 0:
    if all():
        break
    for _ in range(len(q)):
        z, x, y = q.popleft()

        for i in range(6):
            z_ = z + dz[i]
            x_ = x + dx[i]
            y_ = y + dy[i]

            if 0<= z_ < h and 0<= x_ < n and 0<= y_ < m:
                if (z_,x_,y_) not in check.keys() and mat[z_][x_][y_] == 0:
                    check[(z_,x_,y_)] = 1
                    mat[z_][x_][y_] = 1
                    q.append((z_,x_,y_))
    answer += 1

if all():
    print(answer)
else:
    print(-1)
