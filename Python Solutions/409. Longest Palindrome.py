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
                # take only even count
                ans+=value-1
                flag=True
        # take odd count of any one (odd occurring character)
        if flag:
            ans+=1
        return ans
