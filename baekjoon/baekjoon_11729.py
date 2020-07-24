import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import math

def hanoi(n, start,goal,help):
    global num
    if n==1:
        #print(f'{start} {goal}')
        num.append((start,goal))
        return
    hanoi(n-1,start,help,goal)
    #print(f'{start} {goal}')
    num.append((start,goal))
    #num+=1
    hanoi(n-1,help,goal,start)

num = []
n = int(read())

hanoi(n,1,3,2)
print(len(num))
for x,y in num:
    print(f'{x} {y}')