import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"[a-z]+", paragraph.lower())
        freq = {}
        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        return max(freq, key=freq.get)