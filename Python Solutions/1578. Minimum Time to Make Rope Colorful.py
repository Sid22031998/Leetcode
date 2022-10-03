class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time=0
        i=1
        size=len(colors)
        if size<=1:
            return 0
        prev=[colors[0], neededTime[0]]
        while i<size:
            if colors[i]==prev[0]:
                if neededTime[i]<=prev[1]:
                    time+=neededTime[i]
                else:
                    time+=prev[1]
                    prev=[colors[i], neededTime[i]]
            else:
                prev=[colors[i], neededTime[i]]
            i+=1
        return time
