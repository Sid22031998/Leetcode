class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        r=''
        flag=1
        for i in s:
            if i=='6' and flag:
                r+='9'
                flag=0
            else:
                r+=i
        return int(r)
