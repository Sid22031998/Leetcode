class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        last=ord(s[0])
        max_count=1
        curr_count=1
        for  i in range(1, len(s)):
            if int(ord(s[i])-last)==1:
                curr_count+=1
            else:
                curr_count=1
            max_count=max(max_count, curr_count)
            last=ord(s[i])
        return max_count
