def binary(A,n,k):
    l=0;
    h=n-1;
    while(l<=h):
        mid=int((l+h)/2)
        if(A[mid]==k):
            return mid
        else:
            if(k>A[mid]):
                l=mid+1
            else:
                h=mid-1
    return -1
print("Enter elements in ascending order")
li=[int(x) for x in input().split()]
k=int(input("enter element to search "))
res=binary(li,len(li),k)
if(res==-1):
    print(k," is not found")
else:
    print(k," is found @ position ",res+1)
