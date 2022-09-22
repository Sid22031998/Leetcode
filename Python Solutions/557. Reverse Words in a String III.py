class Solution:
    def reverseWords(self, s: str) -> str:
        ans=''
        i=0
        n=len(s)
        for j in range(n):
            if s[j]==' ':
                ans+=s[i:j][::-1]+' '
                i=j+1
        ans+=s[i:][::-1]
        return ans
