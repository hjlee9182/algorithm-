import collections
def check(ice):
    t = 0
    while True:

        t+=1
        ice2 = []
        zero = []
        for x,y in ice:

            damage = 0
            for i in range(4):
                x_ = x+dx[i]
                y_ = y+dy[i]
                if 0<=x_<n and 0<=y_<m:
                    if mat[x_][y_]==0:
                        damage +=1
            if mat[x][y]>damage:
                mat[x][y]-=damage
                ice2.append((x,y))
            else:
                zero.append((x,y))
        for x,y in zero:
            mat[x][y] = 0

        visit = [[0 for i in range(m)] for j in range(n)]

        many = 0
        for x,y in ice2:
            if visit[x][y]==1:
                continue
            else:
                q = collections.deque()
                q.append((x,y))

                while len(q)>0:
                    x1,y1 = q.popleft()
                    visit[x1][y1] = 1
                    for i in range(4):
                        x_ = x1+dx[i]
                        y_ = y1+dy[i]
                        if 0<=x_<n and 0<=y<m:
                            if mat[x_][y_]>0 and visit[x_][y_]==0:
                                q.append((x_,y_))
                                visit[x_][y_] = 1
                many+=1
        ice = ice2
        if many>=2:
            return t
        if len(ice2)==0:
            return 0


n,m = map(int,input().split())

mat = []
ice = []
for i in range(n):
    li = list(map(int,input().split()))
    for j in range(m):
        if li[j]>0:
            ice.append((i,j))
    mat.append(li)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

print(check(ice))


