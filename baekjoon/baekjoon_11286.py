import heapq
import sys
read = lambda :sys.stdin.readline().strip()
n = int(read())

mat = []

for i in range(n):
    num = int(read())
    if num==0:
        if len(mat)==0:
            print(0)
        else:
            out = heapq.heappop(mat)
            print(out[1])
    else:
        abs_num = abs(num)
        heapq.heappush(mat,(abs_num,num))
