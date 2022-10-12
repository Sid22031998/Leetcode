class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n=len(nums)
        for i in range(n-2):
            third_side=nums[i]
            for j in range(i+1, n-1, 2):
                if nums[j]+nums[j+1]>third_side:
                    return third_side+nums[j]+nums[j+1]
        return 0
