class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        evenSum=0
        for num in nums:
            if num%2==0:
                evenSum+=num
        for query in queries:
            val=query[0]
            index=query[1]
            if nums[index]%2==0:
                if (nums[index]+val)%2==0:
                    evenSum+=val
                else:
                    evenSum-=nums[index]
            else:
                if (nums[index]+val)%2==0:
                    evenSum+=val+nums[index]
            nums[index]+=val
            # temp=0
            # for num in nums:
            #     if num%2==0:
            #         temp+=num
            ans.append(evenSum)
        return ans
