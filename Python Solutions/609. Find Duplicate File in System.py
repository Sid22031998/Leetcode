class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d={}
        for path in paths:
            path_list=path.split(' ')
            for each_path in path_list[1:]:
                file=each_path.split('(')
                if file[1][:-1] in d:
                    d[file[1][:-1]].append(path_list[0]+'/'+file[0])
                else:
                    d[file[1][:-1]]=[path_list[0]+'/'+file[0]]
        ans=[]
        for key, value in d.items():
            if len(value)>1:
                ans.append(value)
        return ans
