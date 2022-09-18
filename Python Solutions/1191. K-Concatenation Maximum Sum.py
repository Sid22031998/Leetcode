class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def kadaneHelp(arr):
            max_sum=0
            curr_sum=0
            n=len(arr)
            for i in range(n):
                curr_sum+=arr[i]
                max_sum=max(max_sum, curr_sum)
                if curr_sum<0:
                    curr_sum=0
            return max_sum
        
        mod=1e9+7
        kadane=kadaneHelp(arr)
        arr_sum=sum(arr)
        if k==1:
            return int(kadane%mod)
        elif arr_sum == kadane:
            return int(kadane*k%mod)
        else:
            # following hints ;)
            return int(max(0, (k-2)*max(arr_sum, 0) + kadaneHelp(arr+arr))%mod)
