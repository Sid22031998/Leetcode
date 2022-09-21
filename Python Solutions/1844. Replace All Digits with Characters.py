class Solution:
    def replaceDigits(self, s: str) -> str:
        r=''
        n=len(s)
        for i in range(n):
            if i%2!=0:
                # print(ord(s[i-1])+int(s[i]))
                r+=chr(ord(s[i-1])+int(s[i]))
            else:
                r+=s[i]
        return r
