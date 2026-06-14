# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        maxWay = -float("inf")
        n = len(nums)
        for i in range(n // 2):
            maxWay = max(nums[i] + nums[n - i - 1], maxWay)
        return maxWay