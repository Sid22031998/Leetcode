class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # Bit Manipulation: TLE (eg. -1, 1)
        # while b:
        #     carry=(a&b)<<1    # to carry it forward
        #     a=a^b             # it acts a sum
        #     b=carry
        # return a
        
        # Way around ;)
        return sum([a,b])
        
