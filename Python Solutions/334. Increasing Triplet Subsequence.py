class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Brute Force
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i]<nums[j]:
        #             for k in range(j+1, n):
        #                 if nums[j]<nums[k]:
        #                     return True
        # return False

        # Optimised
        a,b=1e11,1e11
        for num in nums:
            if b<num:
                return True
            if a>=num:
                a=num
            else:
                b=num
        return False        
