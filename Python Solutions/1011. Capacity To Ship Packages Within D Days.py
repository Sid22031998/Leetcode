class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isPossible(value):
            s=0
            count=0
            for weight in weights:
                s+=weight
                if s>value:
                    s=weight
                    count+=1
                    if s>value:
                        return False
            # print(count)
            if count<days:
                return True
            return False

        low=min(weights)
        high=sum(weights)
        ans=high
        while low<=high:
            mid=(low+high)//2
            # print(mid)
            if isPossible(mid):
                ans=mid
                # print(mid)
                high=mid-1
            else:
                low=mid+1
        # print(isPossible(15))
        return ans
