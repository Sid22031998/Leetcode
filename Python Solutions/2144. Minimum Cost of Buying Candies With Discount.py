class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n=len(cost)
        if n<=2:
            return sum(cost)
        i=n-1
        ans=0
        while i>0:
            print(cost[i-1], cost[i])
            ans+=cost[i-1]+cost[i]
            i-=3
        if i==0:
            ans+=cost[0]
        return ans
