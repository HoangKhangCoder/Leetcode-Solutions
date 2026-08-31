# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        points = []
        cur = head
        i = 1
        while cur.next and cur.next.next:
            a, b, c = cur.val, cur.next.val, cur.next.next.val
            if (a > b and b < c) or (a < b and b > c):
                points.append(i + 1)
            cur = cur.next
            i += 1
        if len(points) < 2:
            return [-1, -1]

        minDis, maxDis = float("inf"), points[-1] - points[0]
        for i in range(len(points) - 1):
            dis = points[i + 1] - points[i]
            minDis = min(minDis, dis)
        return [minDis, maxDis]