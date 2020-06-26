pos=-1


def search(arr,n):

    l=0
    u=len(arr)-1
    while l<=u:
        mid=(l+u)//2
        if arr[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if arr[mid]<n:
                l=mid;
            else:
                u=mid
    return False






arr=[5,8,4,6,9,2]
arr.sort()
n=int(input("enter a number to be searched"))

if search(arr,n):
    print("found at ",pos+1)
else:
    print("not found")