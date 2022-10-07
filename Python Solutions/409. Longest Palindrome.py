class Solution:
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        ans=1
        count=Counter(s)
        # print(count)
        ans=0
        flag=False
        for value in count.values():
            if value%2==0:
                ans+=value
            else:
                ans+=value-1
                flag=True
        if flag:
            ans+=1
        return ans
