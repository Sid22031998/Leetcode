class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def helper(ind, cut):
            if cut==d:
                return max(jobDifficulty[ind:])
            curr=-1e9
            ans=1e9
            for i in range(ind, n-d+cut):
                curr=max(curr, jobDifficulty[i])
                ans=min(ans, curr+helper(i+1, cut+1))
            return ans
        n=len(jobDifficulty)
        if n<d:
            return -1
        return helper(0, 1)
