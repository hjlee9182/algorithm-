

n, m = map(int,input().split())

mat= []
for i in range(n):
    mat.append(input())

for j in range(m-1,-1,-1):
    strt =''
    for i in range(n):
        if mat[i][j]=='.':
            strt+='.'
        elif mat[i][j]=='O':
            strt+='O'
        elif mat[i][j]=='-':
            strt+='|'
        elif mat[i][j]=='|':
            strt+='-'
        elif mat[i][j]=='/':
            strt+="\\"
        elif mat[i][j]=='\\':
            strt+='/'
        elif mat[i][j]=='^':
            strt+='<'
        elif mat[i][j]=='<':
            strt+='v'
        elif mat[i][j]=='v':
            strt+='>'
        elif mat[i][j]=='>':
            strt+='^'
    print(strt)