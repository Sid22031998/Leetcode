class Solution:
    def nextGreaterElement(self, n: int) -> int:
        org=n
        n=str(n)
        arr=list(n)
        # print(arr)
        i=len(arr)-1
        while i>0 and arr[i]<=arr[i-1]:
            i-=1
        if i==0:
            return -1
        j=len(arr)-1
        while j>i and arr[j]<=arr[i-1]:
            j-=1
        arr[j],arr[i-1]=arr[i-1],arr[j]
        arr[i:]=arr[i:][::-1]
        n=int(''.join(arr))
        if n>org and n<2**31:
            return n
        return -1
