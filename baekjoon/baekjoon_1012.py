import sys
sys.setrecursionlimit(50000)
def sol(x,y):
	mat[x][y]= 0
	for i in range(4):
		mx = dx[i]+x
		my = dy[i]+y
		if (0<=mx<n and 0<=my<m and mat[mx][my]==1):
			sol(mx,my)
t= int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(t):
	m,n,k=map(int,input().split())
	mat=[[0]*m for i in range(n)]
	for i in range(k):
		a,b = map(int,input().split())
		mat[b][a] = 1
	ans=0
	for i in range(n):
		for j in range(m):
			if (mat[i][j]==1):
				sol(i,j)
				ans+=1
	print(ans)