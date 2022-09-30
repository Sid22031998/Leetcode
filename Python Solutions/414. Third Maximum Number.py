class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        d={}
        ans=[]
        for num in nums:
            if num not in d:
                d[num]=1
                ans.append(num)
        
        if len(ans)>2:
            return ans[-3]
        return ans[-1]


# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         s=sorted(list(set(nums)))
#         if len(s)>2:
#             return s[-3]
#         return s[-1]
