class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        a,b,c=0,1,1
        ans=a+b+c
        for i in range(2, n):
            ans=a+b+c
            a=b
            b=c
            c=ans
        return ans
