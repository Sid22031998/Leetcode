class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count=Counter(tasks)
        ans=0
        # print(count)
        for value in count.values():
            if value==1:
                return -1
            else:
                div,rem=divmod(value, 3)
                if rem==0:
                    ans+=div
                else:
                    ans+=div+1
        return ans
