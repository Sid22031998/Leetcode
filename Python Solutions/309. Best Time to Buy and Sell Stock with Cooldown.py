class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for i in range(n+1)]

        def helper(ind, prevInd, buy):
            if ind>=n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            take, notTake = 0, 0
            if not buy:
                notTake = max(prices[ind] + helper(ind+2, ind, 1), helper(ind+1, prevInd, buy))
            if prevInd==-1 or buy:
                take = max(-prices[ind] + helper(ind+1, ind, 0), helper(ind+1, prevInd, buy))
            dp[ind][buy] = max(take, notTake)
            return dp[ind][buy]
        
        return helper(0, -1, 1)
