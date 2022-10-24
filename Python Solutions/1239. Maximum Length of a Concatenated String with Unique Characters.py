class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n=len(arr)
        def helper(ind, prev):
            if ind==n:
                return 0
            notTake=helper(ind+1, prev)
            take=0
            count=Counter(arr[ind]+prev)
            # print(count)
            flag=True
            temp=''
            for key, value in count.items():
                temp+=key
                if value>1:
                    flag=False
                    break
            if flag:
                take=max(len(count), helper(ind+1, temp))
                # print(take)
            ans=max(take, notTake)
            return ans
        return helper(0, '')
                    
