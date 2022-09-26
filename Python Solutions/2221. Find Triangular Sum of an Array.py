class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        
        # base conditions
        if n==0:
            return 0
        if n<=2:
            return sum(nums)%10
        
        # we will iterate over nums list 
        # keep updating the sum in the same list 
        # pop from the end (to reduce the list just like a triangle)
        while len(nums)>1:
            temp=nums[-1]
            for j in range(len(nums)-2, -1, -1):
                a=nums[j]
                nums[j]=(nums[j]+temp)%10   #element constraint: 0<=nums[i]<=9 
                temp=a
            nums.pop()
        # print(nums)
        return nums[0]
