class Solution:
    def makeGood(self, s: str) -> str:
        # print(chr(ord('A')+32))
        stack=[]
        for char in s:
            if stack:
                if stack[-1]==chr(ord(char)-32) or stack[-1]==chr(ord(char)+32):
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)
