class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        n=len(strs)
        for i in range(n):
            s=strs[i]
            s="".join(sorted(s))
            # print(s)
            if s in d:
                d[s].append(strs[i])
            else:
                d[s]=[strs[i]]
        ans=[]
        for value in d.values():
            ans.append(value)
        return ans
