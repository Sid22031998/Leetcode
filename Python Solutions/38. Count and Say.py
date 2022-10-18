class Solution:
    def countAndSay(self, n: int) -> str:
        last='1'
        for i in range(2, n+1):
            temp=''
            prev=last[0]
            count=1
            for i in range(1, len(last)):
                if last[i]==prev:
                    count+=1
                else:
                    temp+=str(count)+last[i-1]
                    prev=last[i]
                    count=1
            temp+=str(count)+last[-1]
            print(temp)
            last=temp
        return last
