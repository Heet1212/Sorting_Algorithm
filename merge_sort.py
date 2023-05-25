def sort(A,l,r):

    if l==r:
        return 
    mid=(l+r)//2
    sort(A,l,mid)
    sort(A,mid+1,r)
    merge(A,l,mid,r)
 
def merge(A,l,mid,r):
    n=mid-l+1
    m=r-mid
    b=[0]*n
    c=[0]*m
    for i in range(l,mid+1):
        b[i-l]=A[i]
        
    for j in range(mid+1,r+1):
        c[j-mid-1]=A[j]   
        print(c[j-mid-1]) 
    i=0
    j=0
    for k in range(l,r+1):
        if i==n:
            A[k]=c[j]
            j+=1
        elif j==m or b[i]<=c[j]:
            A[k]=b[i]
            i+=1
        else:
            A[k]=c[j]
            j+=1
         

A=[2,4,3,5,7]

sort(A,0,len(A)-1)
print(A)

                

       





    
