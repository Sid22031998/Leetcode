import math
class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for a in range(1, n+1):
            for b in range(1, n+1):
                left=math.sqrt(a*a+b*b)
                if left<=n:
                    low=1
                    high=n
                    while low<=high:
                        mid=(low+high)//2
                        if float(mid)==left:
                            count+=1
                            break
                        elif mid>left:
                            high=mid-1
                        else:
                            low=mid+1
        return count
