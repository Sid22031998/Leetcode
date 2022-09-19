class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        def helper(ind, k, currSum, count):
            if ind>=n:
                return 0
            if k==0:
                return -int(1e9)
            if dp[ind][count][k]!=-1:
                return dp[ind][count][k]
            currSum+=nums[ind]
            notTake=currSum/count + helper(ind+1, k-1, 0, 1)
            take=helper(ind+1, k, currSum, count+1)
            dp[ind][count][k]=max(take, notTake)
            return dp[ind][count][k]
        
        n=len(nums)
        dp=[[[-1]*(k+1) for i in range(n+1)] for i in range(n+1)]
        return helper(0, k, 0, 1)
        
                
