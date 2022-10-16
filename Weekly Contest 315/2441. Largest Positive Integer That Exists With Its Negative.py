class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            d[num]=1
        maxi=-1e9
        for num in nums:
            if num>maxi and -num in d:
                maxi=num
        if maxi==-1e9:
            return -1
        return maxi
                
        
