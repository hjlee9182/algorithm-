

def hi(bloomDay,m,k):

    if m*k>len(bloomDay):
        return -1

    left,right = 1, max(bloomDay)

    while left<right:

        mid = (left+right)//2

        flower,bouqet = 0,0

        for i in bloomDay:
            if i>mid:
                flower=0
            else:
                flower +=1

            if flower==k:
                flower = 0
                bouqet+=1
            if bouqet==m:
                break

        if bouqet==m:
            right = mid
        else:
            left = mid+1
    return left


print(hi([1000000000,1000000000],1,1))