class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        flower=[]
        n=len(plantTime)
        for i in range(n):
            flower.append([plantTime[i], growTime[i]])
        flower.sort(key=lambda x: x[1], reverse=True)
        time=0
        plant=0
        for i, j in flower:
            plant+=i
            time=max(time, plant+j)
        return time
