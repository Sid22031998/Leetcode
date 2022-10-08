class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s=['a']*n
        value=n
        i=n-1
        while value<k:
            if k-value-1>=25:
                value+=26-1
                s[i]='z'
            else:
                val=k-value
                # print(val)
                char=chr(ord('a')+val)
                value+=k-1
                s[i]=char
            i-=1
        return ''.join(s)
