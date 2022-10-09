class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        logs.sort(key = lambda x : x[1])
        maxi=logs[0][1]
        prev=maxi
        ans=logs[0][0]
        # print(logs)
        for i in range(1, len(logs)):
            # print(logs[i][1]-prev, maxi)
            if logs[i][1]-prev==maxi:
                ans=min(ans, logs[i][0])
            if logs[i][1]-prev>maxi:
                maxi=logs[i][1]-prev
                ans=logs[i][0]
                # print(ans)
            prev=logs[i][1]
        return ans
