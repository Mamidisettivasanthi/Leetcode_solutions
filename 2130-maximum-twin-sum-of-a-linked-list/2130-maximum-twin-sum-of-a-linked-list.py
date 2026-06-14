class Solution:
    def pairSum(self, head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        left = 0
        right = len(arr) - 1

        ans = 0

        while left < right:
            ans = max(ans, arr[left] + arr[right])

            left += 1
            right -= 1

        return ans