class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range(2*n-1, -1, -1):
            while len(stack) and stack[-1]<=nums[i%n]:
                stack.pop()
            if i<n:
                if len(stack):
                    ans[i]=stack[-1]
            stack.append(nums[i%n])
        return ans
