class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        ans=[]
        i=1
        j=0
        while stack!=target:
            stack.append(i)
            ans.append('Push')
            if stack[-1]!=target[j]:
                stack.pop()
                ans.append('Pop')
                j-=1
            i+=1
            j+=1
        return ans
