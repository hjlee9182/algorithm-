import sys
read = lambda :sys.stdin.readline().strip()


n = int(read())

cost = list(map(int,read().split()))
cost.append(0)
city = list(map(int,read().split()))
d = [0 for i in range(n)]

d[0] = cost[0]*city[0]
cheap = city[0]
for i in range(1,n):
    if city[i]<cheap:
        cheap = city[i]
    d[i] = d[i-1]+cheap*cost[i]
print(d[n-1])