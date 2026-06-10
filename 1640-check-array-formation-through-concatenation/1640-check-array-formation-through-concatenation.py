class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {}
        for piece in pieces:
            mp[piece[0]] = piece
        i = 0
        while i < len(arr):
            if arr[i] not in mp:
                return False
            piece = mp[arr[i]]
            for num in piece:
                if i >= len(arr) or arr[i] != num:
                    return False
                i += 1
        return True