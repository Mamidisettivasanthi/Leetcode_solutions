from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str],
                      wordsQuery: List[str]) -> List[int]:

        # Trie node:
        # children -> next characters
        # index -> index of the best word
        trie = [{"children": {}, "index": 0}]

        # Word with shortest length
        best = 0

        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[best]):
                best = i

        # Build trie using reversed words
        for i, word in enumerate(wordsContainer):

            node = 0

            # If this word is shorter, it becomes the best
            if len(word) < len(wordsContainer[trie[node]["index"]]):
                trie[node]["index"] = i

            for ch in reversed(word):

                if ch not in trie[node]["children"]:
                    trie[node]["children"][ch] = len(trie)
                    trie.append({
                        "children": {},
                        "index": i
                    })

                node = trie[node]["children"][ch]

                # Keep shortest word for this suffix
                if len(word) < len(wordsContainer[trie[node]["index"]]):
                    trie[node]["index"] = i

        ans = []

        for word in wordsQuery:

            node = 0

            for ch in reversed(word):

                if ch not in trie[node]["children"]:
                    break

                node = trie[node]["children"][ch]

            ans.append(trie[node]["index"])

        return ans