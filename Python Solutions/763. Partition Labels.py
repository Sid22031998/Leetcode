class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count=Counter(s)
        prev={}
        ans=[]
        n=len(s)
        last=0
        for i in range(n):
            if s[i] in prev:
                prev[s[i]]+=1
            else:
                prev[s[i]]=1
            # check if all the occurences are done
            if prev[s[i]]==count[s[i]]:
                del prev[s[i]]
            # if dict is empty then we have a partition
            if len(prev)==0:
                ans.append(i-last+1)
                last=i+1
        return ans
            
