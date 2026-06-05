class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        s = nums1 + nums2
        s.sort()
        n = len(s)
        if n % 2 == 1:
            return s[n // 2]
        return (s[n // 2 - 1] + s[n // 2]) / 2