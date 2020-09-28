import sys

read = lambda : sys.stdin.readline().strip()

n,m,x,y = map(int,read().split())

mat = [1234567891234 for i in range(n)]

d =dict()
for _ in range(n):
    d[_] = []
for _ in range(m):
    a,b,c = map(int,read().split())
    li = d[a]
    li.append((c,b))
    li = d[b]
    li.append((c,a))

visit = [0 for i in range(n)]
visit[y] = 1
mat[y] = 0
for q in range(n):
    li = d[y]
    for value,node in li:
        if mat[y]+value<mat[node] and visit[node]==0:
            mat[node] = mat[y]+value
    now = 1234567891234
    for i in range(n):
        if mat[i]<now and visit[i]==0:
            now = mat[i]
            y = i
    visit[y] = 1
mat.sort()
day = 0
s  = x

for i in range(1,n):
    if mat[i]==1234567891234:
        print(-1)
        sys.exit()
    if s >= mat[i]*2 :
        s-=mat[i]*2
    else:
        day+=1
        s = x
        if s >= mat[i]*2:
            s-=mat[i]*2
        else:
            print(-1)
            sys.exit()
    if i == n - 1:
        day += 1
print(day)
