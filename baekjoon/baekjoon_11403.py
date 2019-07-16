import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

num = int(read())

mat = [ list(map(int, list(read().split(' ')))) for _ in range(num)]

for k in range(num):
    for i in range(num):
        for j in range(num):
            if mat[i][k] and mat[k][j]:
                mat[i][j] = 1

for i in range(num):
    _str = ""
    for j in range(num):
        _str+= str(mat[i][j])+ " "
    print(_str)