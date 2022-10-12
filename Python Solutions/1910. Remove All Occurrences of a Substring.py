class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        n=len(s)
        m=len(part)
        part=list(part)
        for i in range(n):
            stack.append(s[i])
            # print(stack[-m:])
            if len(stack)>=m and stack[-m:]==part:
                for j in range(m):
                    stack.pop()
        return ''.join(stack)
