# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        @cache
        def countNodes(root):
            if not root:
                return 0
            return 1 + max(countNodes(root.left), countNodes(root.right))
        
        left_branch = countNodes(root.left)
        right_branch = countNodes(root.right)
        if abs(left_branch - right_branch) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)