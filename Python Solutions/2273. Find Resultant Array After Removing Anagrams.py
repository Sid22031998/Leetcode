class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        start=0
        while start<len(words)-1:
            curr=list(words[start])
            nxt=list(words[start+1])
            curr.sort()
            nxt.sort()
            if nxt==curr:
                words.pop(start+1)
            else:
                start+=1
        return words
