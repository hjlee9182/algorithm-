import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import copy
n= int(read())
sx,sy = [0]*2
dx = [1,-1,0,0]
dy = [0,0,1,-1]
test = [0]*1000

def bfs():
    people.append((sx,sy))
    while (fire or people):
        pz = len(people)
        fz = len(fire)
        while fz != 0:
            x, y = fire.popleft()
            for _ in range(4):
                nx = dx[_] + x
                ny = dy[_] + y
                if 0<=nx<b and 0<=ny<a and (mat[nx][ny] == '.' or mat[nx][ny] == '@'):
                    mat[nx][ny] = '*'
                    fire.append((nx, ny))

            fz = fz - 1

        while pz != 0:
            x, y = people.popleft()
            for _ in range(4):
                nx = dx[_] + x
                ny = dy[_] + y
                if nx < 0 or ny < 0 or nx >= b or ny >= a:
                    print(visit[x][y] + 1)
                    return ;
                if mat[nx][ny] == '.':
                    mat[nx][ny] = '@'
                    visit[nx][ny] = visit[x][y] + 1
                    people.append((nx, ny))
            pz -= 1
    print("IMPOSSIBLE")




for _ in range(n):
    a,b = map(int,read().split())
    fire = deque()
    people = deque()
    mat = [ list(map(str, list(read()))) for _ in range(b)]
    visit = [[0]*a for _ in range(b)]
    for i in range(b):
        for j in range(a):
            if mat[i][j] == '*' :
                fire.append((i,j))
            if mat[i][j] == '@':
                sx,sy= i,j
    bfs()