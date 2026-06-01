class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for num in nums1:
            idx = nums2.index(num)
            greater = -1
            for i in range(idx + 1, len(nums2)):
                if nums2[i] > num:
                    greater = nums2[i]
                    break
            ans.append(greater)
        return ans