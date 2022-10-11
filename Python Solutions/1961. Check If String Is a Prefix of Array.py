class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        j=0
        ind=0
        n=len(s)
        m=len(words)
        for i in range(n):
            if s[j:i+1]==words[ind]:
                ind+=1
                j=i+1
            if ind==m:
                break
        if j==n:
            return True
        return False
