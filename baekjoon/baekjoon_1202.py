import sys
read = lambda : sys.stdin.readline().strip()
import heapq

n,k = map(int,read().split())

dia = []
for _ in range(n):
    a = list(map(int,read().split()))
    dia.append(a)
check = []
for _ in range(k):
    check.append(int(read()))
dia.sort()
check.sort()

max_heap=[]
j = 0
result = 0
for i in range(k):

    while j<n and check[i]>=dia[j][0]:
        heapq.heappush(max_heap,-dia[j][1])
        j+=1

    if len(max_heap)>0:
        b = heapq.heappop(max_heap)
        result+=abs(b)
print(result)



