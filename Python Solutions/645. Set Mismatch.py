class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count=Counter(nums)
        ans=[0,0]
        for i in range(1, n+1):
            if i not in count:
                ans[-1]=i
                continue
            if count[i]==2:
                ans[0]=i
        return ans
