class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        count=0
        arr=[]
        for word in s1:
            if s1.count(word)==1 and word not in s2:
                arr.append(word)
        for word in s2:
            if s2.count(word)==1 and word not in s1:
                arr.append(word)
        return arr



        