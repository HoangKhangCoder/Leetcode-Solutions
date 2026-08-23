# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Idea: add two numbers represented as linked lists, where each node
        # stores a single digit ordered from the least significant digit to
        # the most significant. We walk both lists in parallel, adding each
        # pair of digits together with the carry from the previous step,
        # exactly like adding two integers by hand.
        resultHead = None   # first node of the result list
        carry = 0            # carry when the sum of two digits >= 10
        tail = None           # pointer to the last node built so far in the result
        node1, node2 = l1, l2
        while node1 or node2 or carry:
            # If list 1 has run out, treat its current digit as 0
            if node1:
                digit1 = node1.val
                node1 = node1.next
            else:
                digit1 = 0

            # If list 2 has run out, treat its current digit as 0
            if node2:
                digit2 = node2.val
                node2 = node2.next
            else:
                digit2 = 0

            # Sum of the current digits: the remainder becomes the result digit,
            # the quotient becomes the new carry
            res, carry = (digit1 + digit2 + carry) % 10, (digit1 + digit2 + carry) // 10

            # Append the new result node to the end of the list being built
            if resultHead:
                tail.next = ListNode(res)
                tail = tail.next
            else:
                resultHead = ListNode(res)
                tail = resultHead
        return resultHead