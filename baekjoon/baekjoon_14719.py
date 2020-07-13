import sys
read = lambda :sys.stdin.readline().strip()

n,m = map(int,read().split())
mat = list(map(int,read().split()))

result = 0

for h in range(len(mat)):
    left = max(mat[:h+1])
    right = max(mat[h:])
    low = min(left,right)
    result+= abs(mat[h]-low)
print(result)