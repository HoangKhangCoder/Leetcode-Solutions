# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, mini = -float("inf"), maxi = float("inf")):
            if not root:
                return True
            if root.val <= mini or root.val >= maxi:
                return False
            return (
                check(root.left, mini, min(root.val, maxi)) and
                check(root.right, max(root.val, mini), maxi)
            )
        return check(root)