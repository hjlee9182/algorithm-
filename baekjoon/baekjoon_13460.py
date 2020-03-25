import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import copy
def check(x_r,y_r,x_b,y_b,direction,dx_r,dy_r,dx_b,dy_b):
    if direction==0:
        if x_r<x_b:
            return dx_r,dy_r,dx_b+1,dy_b
        else:
            return dx_r+1, dy_r, dx_b, dy_b
    if direction==2:
        if x_r<x_b:
            return dx_r-1,dy_r,dx_b,dy_b
        else:
            return dx_r, dy_r, dx_b-1, dy_b
    if direction==1:
        if y_r<y_b:
            return dx_r,dy_r-1,dx_b,dy_b
        else:
            return dx_r, dy_r, dx_b, dy_b-1
    if direction==3:
        if y_r<y_b:
            return dx_r,dy_r,dx_b,dy_b+1
        else:
            return dx_r, dy_r+1, dx_b, dy_b


def go(direction,mat,x,y):
    if direction==0:
        while True:
            dx = x-1
            if dx<0 or dx>=m:
                return x,y
            if mat[dx][y] =='#':
                return x,y
            if mat[dx][y] =='O':
                return -1,-1
            x = x-1
    if direction==2:
        while True:
            dx = x+1
            if dx<0 or dx>=m:
                return x,y
            if mat[dx][y] =='#':
                return x,y
            if mat[dx][y] =='O':
                return -1,-1
            x = x+1
    if direction==1:
        while True:
            dy = y+1
            if dy<0 or dy>=n:
                return x,y
            if mat[x][dy] =='#':
                return x,y
            if mat[x][dy] =='O':
                return -1,-1
            y = y+1
    if direction==3:
        while True:
            dy = y-1
            if dy<0 or dy>=n:
                return x,y
            if mat[x][dy] =='#':
                return x,y
            if mat[x][dy] =='O':
                return -1,-1
            y = y-1

def find():
    global R
    global B
    count= [1]
    fake = copy.deepcopy(mat)
    m = [fake]
    z,x = R[0]
    c,v = B[0]

    old_list = [(z,x,c,v)]
    while len(R)!=0:

        count_  = count.pop(0)
        if count_>10:
            for i in count:
                if i<=10:
                    break
                else :
                    return -1
        x_r,y_r = R.pop(0)
        x_b,y_b = B.pop(0)
        mat_ = m.pop(0)
        for i in range(4):
            mat_2 = copy.deepcopy(mat_)
            dx_r,dy_r = go(i,mat_2,x_r,y_r)
            dx_b,dy_b = go(i,mat_2,x_b,y_b)

            if dx_r == -1 and dy_r ==-1:
                if dx_b == -1 and dy_b ==-1:
                    continue
                return count_
            else :
                if dx_b == -1 and dy_b == -1:
                    continue

            if dx_r==dx_b and dy_r ==dy_b:
                dx_r,dy_r,dx_b,dy_b = check(x_r,y_r,x_b,y_b,i,dx_r,dy_r,dx_b,dy_b)
            if ((dx_r == x_r) and (dy_r == y_r)) and ((dx_b == x_b) and (dy_b == y_b)) :
                continue
            if (dx_r,dy_r,dx_b,dy_b) in old_list:
                continue


            mat_2[x_r][y_r] = '.'
            mat_2[x_b][y_b]= '.'
            mat_2[dx_r][dy_r] = 'R'
            mat_2[dx_b][dy_b] = 'B'
            R.append((dx_r,dy_r))
            B.append((dx_b,dy_b))
            old_list.append((dx_r,dy_r,dx_b,dy_b))
            count.append(count_+1)
            m.append(mat_2)
    return -1


m,n = map(int,read().split())
mat = []
for i in range(m):
    mat.append(list(read())[1:-1])
mat = mat[1:-1]
m,n = m-2,n-2
R = []
B = []
for i in range(m):
    for j in range(n):
        if mat[i][j]=='R':
            R.append((i,j))
            #mat[i][j] ='.'
        if mat[i][j]=='B':
            B.append((i,j))
            #mat[i][j] = '.'

q = find()
if q<=10:
    print(q)
else:
    print(-1)