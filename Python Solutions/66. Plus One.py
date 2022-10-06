class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i]=str(digits[i])
        digit=int(''.join(digits))+1
        ans=[]
        for d in str(digit):
            ans.append(int(d))
        return ans
        
