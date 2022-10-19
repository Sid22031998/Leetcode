class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        count=dict(sorted(count.items(), key=lambda item: (-item[1], item[0])))
        # print(count)
        ans=[]
        prev_value=-1
        temp=[]
        for key in count.keys():
            k-=1
            # print(key)
            ans.append(key)
            if k==0:
                break
        # ans.sort()
        return ans
