import sys
import itertools
read = lambda : sys.stdin.readline().strip()
import copy
mat = [
    [2,1,2,3,4,5],
    [4,2,3,4,5,6],
    [6,3,4,5,6,7],
    [8,4,5,6,7,8],
    [10,20,21,22,25,29],
    [12,6,7,8,9,10],
    [14,7,8,9,10,11],
    [16,8,9,10,11,12],
    [18,9,10,11,12,13],
    [20,23,24,25,29,30],
    [22,11,12,13,14,15],
    [24,12,13,14,15,16],
    [26,13,14,15,16,17],
    [28,14,15,16,17,18],
    [30,26,27,28,25,29],
    [32,16,17,18,19,31],
    [34,17,18,19,31,31],
    [36,18,19,31,31,31],
    [38,19,31,31,31,31],
    [40,31,31,31,31,31],
    [13,21,22,25,29,30],
    [16,22,25,29,30,19],
    [19,25,29,30,19,31],
    [22,24,25,29,30,19],
    [24,25,29,30,19,31],
    [25,29,30,19,31,31],
    [28,27,28,25,29,30],
    [27,28,25,29,30,19],
    [26,25,29,30,19,31],
    [30,30,19,31,31,31],
    [35,19,31,31,31,31],
    [0,31,31,31,31,31]
]
def dfs(num,summ,status):
    global result,number
    if num==10:
        result = max(result,summ)
        return
    for i in range(4):
        if status[i]==31:
            continue
        if status[i]==-1:
            check = status[i]+number[num]
        else:
            check = mat[status[i]][number[num]]

        if (check in status)and check!=31:
            continue
        sta2 = copy.deepcopy(status)
        sta2[i] = check
        #print(sta2)
        dfs(num+1,summ+mat[sta2[i]][0],sta2)

result = 0
number = list(map(int,read().split()))

status = [-1 for i in range(4)]
dfs(0,0,status)
print(result)