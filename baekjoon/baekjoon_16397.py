import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def find_max(a) :
    if a==0:
        return 0
    a = a*2
    b=1
    result = 0
    while a>9:
        result+= int(a%10)*b
        b = str(b)+'0'
        b = int(b)
        a  = int(a/10)
    a = (a-1)*b
    return a+result

n,t,g = map(int,read().split())

if n==g:
    print(0)
    sys.exit()

mat = [0]*100000
visit = [0]*100000
q = deque()
q.append(n)
min_num = 10000000000

while q:
    x = q.popleft()

    for i in range(2):
        if i == 0:
            nx = x + 1
        else:
            if 2 * x > 99999:
                continue
            else:
                nx = find_max(x)
        if nx < 0 or nx >99999:
            continue
        if nx == g:
            min_num = min(min_num, mat[x] + 1)
            mat[nx] = min_num

        if mat[nx] == 0 and visit[nx] == 0:
            q.append(nx)
            visit[nx] = 1
            mat[nx] = mat[x] + 1




if mat[g]==0 or mat[g]>t:
    print("ANG")
else:
    print(mat[g])