class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(map(str, s.split(' ')))
        s=list(filter(lambda a: a != '', s))
        # print(s)
        s.reverse()
        return " ".join(s)
