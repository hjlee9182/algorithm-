import collections
import math
def hi(arr,k):

    sort_a = sorted(arr)
    m = sort_a[(len(arr)-1)//2]
    mat =[]
    for i in range(len(arr)):
        mat.append((abs(arr[i]-m),arr[i]))
    mat = sorted(mat)
    mat.reverse()
    result = []
    for i in range(k):
        result.append(mat[i][1])
    return result




print(hi([1,2,3,4,5],2))