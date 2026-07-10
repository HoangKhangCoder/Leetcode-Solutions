# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        carry = 0
        cur = None
        cur1, cur2 = l1, l2
        while cur1 or cur2 or carry:
            if cur1:
                v1 = cur1.val
                cur1 = cur1.next
            else:
                v1 = 0
            
            if cur2:
                v2 = cur2.val
                cur2 = cur2.next
            else:
                v2 = 0
            
            res, carry = (v1 + v2 + carry) % 10, (v1 + v2 + carry) // 10
            if ans:
                cur.next = ListNode(res)
                cur = cur.next
            else:
                ans = ListNode(res)
                cur = ans
        return ans