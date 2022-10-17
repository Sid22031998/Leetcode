class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr=[0]*26
        for letter in sentence:
            arr[ord(letter)-ord('a')]=1
        if 0 in arr:
            return False
        return True
