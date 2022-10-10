class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        if n==1:
            return ''
        
        pal=list(palindrome)
        for i in range(n//2 + 1):
            if pal[i]!='a':
                temp=pal[i]
                pal[i]='a'
                if pal==pal[::-1]:
                    pal[i]=temp
                else:
                    return ''.join(pal)
        pal[-1]='b'
        return ''.join(pal)
