import sys
read = lambda : sys.stdin.readline().strip()

def rot(h,w,mat):
    result = [[ 0 for i in range(h)]for j in range(w)]
    x,y = 0,0

    for j in range(w):
        y = 0
        for i in range(h-1,-1,-1):
            result[x][y] = mat[i][j]
            y = y+1
        x = x+1

    return result

def check(x,y,a,b,stick):
    global mat
    c_list = []
    for i in range(a):
        for j in range(b):
            if 0<=x+i<n and 0<=y+j<m:
                if mat[x+i][y+j]==0 and stick[i][j]==1:
                    c_list.append((x+i,y+j))
                    continue
                elif stick[i][j]==0:
                    continue
                else:
                    return False
            else:
                return False

    for q,w in c_list:
        mat[q][w] = 1
    return True

n,m,k = map(int,read().split())

m_info = []
mat_list = []

for i in range(k):
    a,b = map(int,read().split())
    mat = []
    for i in range(a):
        li = list(map(int,read().split()))
        mat.append(li)
    mat_list.append(mat)
    m_info.append((a,b))

mat = [[0 for i in range(m)]for j in range(n)]

for k_ in range(k):
    a,b = m_info[k_]
    stick = mat_list[k_]
    flag = 0
    for r_num in range(4):
        for i in range(n):
            for j in range(m):
                if check(i,j,a,b,stick):
                    flag = 1
                    break
            if flag==1:
                break
        if flag==1:
            break
        stick = rot(a,b,stick)
        a,b = b,a

answer = 0
for i in range(n):
    for j in range(m):
        if mat[i][j]==1:
            answer+=1
print(answer)
