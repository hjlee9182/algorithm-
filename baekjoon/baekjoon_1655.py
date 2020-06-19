
def b_search(k):
    global mat
    left = 0
    right = len(mat)-1

    while left<=right:
        mid = (left+right)//2

        if k==mat[mid]:
            return mid
        if k<mat[mid]:
            right = mid-1
        else:
            left = mid+1
    return left
n = int(input())


mat  = []
for _ in range(n):
    k = int(input())
    if len(mat)==0:
        mat.append(k)
    else:
        loc = b_search(k)
        mat.insert(loc,k)
    if len(mat)%2==0:
        result = min(mat[len(mat)//2],mat[len(mat)//2-1])
    else:
        result = mat[len(mat)//2]
    print(result)
