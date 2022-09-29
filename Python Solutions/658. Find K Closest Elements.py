class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        n=len(arr)
        for i in range(n):
            heapq.heappush(heap, [abs(arr[i]-x), arr[i]])
        ans=[]
        while k>0:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        ans.sort()
        return ans
