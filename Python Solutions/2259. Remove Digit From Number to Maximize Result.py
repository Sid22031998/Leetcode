class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        arr=[]
        n=len(number)
        for i in range(n):
            if number[i]==digit:
                arr.append(int(number[:i]+number[i+1:]))
        return str(max(arr))
