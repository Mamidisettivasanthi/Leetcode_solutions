class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr=[]
        for word in words:
            for other in words:
                if word!=other and word in other:
                    arr.append(word)
                    break
        return arr
        