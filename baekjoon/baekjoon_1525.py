import sys
from collections import deque
import copy
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

visit = dict()
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():

    q = deque()
    q.append(f_str)
    visit[f_str] = 0
    while q:
        n = q.popleft()
        if n=='123456780':
            return visit[n]
        nine = n.find('0')
        x = nine//3
        y = nine%3
        for i in range(4):
            nx = dx[i]+ x
            ny = dy[i] +y
            if nx<0 or ny<0 or nx>=3 or ny>=3 : continue
            n = list(n)
            new = copy.deepcopy(n)
            next = nx*3+ny
            next_item = n[next]
            new[next] = n[nine]
            new[nine] = next_item
            new = ''.join(new)
            n = ''.join(n)
            if new not in visit:
                visit[new] = visit[n]+1
                q.append(new)
    return -1


mat = [list(map(int,list(read().split()))) for k in range(3)]
f_str =''
for i in range(3):
    for j in range(3):
        f_str+=str(mat[i][j])

print(bfs())