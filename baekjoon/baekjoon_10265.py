import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def dfs(x,y) :
    mat[x][y] = 2
    if x==y :
       return 1
    if y in li :
        return len(li)

    if x in li:
        li
    else :
        li.append(x)
    li.append(y)
    if 1 in mat[y] :
        idx= mat[y].index(1)
    else:
        idx = mat[y].index(2)

    if idx == y:
        return 1 + dfs(y, idx)
    else :
        return dfs(y,idx)

num,m_student = map(int,read().split())

mat = [[0]*(num+1) for i in range(num+1)]

std = list(map(int,read().split()))

for _ in range(1,num+1):
    mat[_][std[_-1]]=1


result = []
for i in range(num+1) :
    for j in range(num+1):
        if mat[i][j] == 1 :
            #mat2 = copy.deepcopy(mat)
            li = []
            size = dfs(i,j)
            result.append(size)

sum_list = sum(result)
result.sort()
result.reverse()
correct =0

for _ in range(len(result)):
    if m_student>=result[_] :
        m_student=m_student-result[_]
        correct+=result[_]
        if m_student == 0 :
            break;
print(correct)