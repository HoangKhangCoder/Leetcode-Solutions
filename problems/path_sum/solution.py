# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(t, tSum):
            if t == None:
                return False
            if t.left == None and t.right == None:
                return tSum == t.val
            else:
                return (traverse(t.left, tSum - t.val)) or (traverse(t.right, tSum - t.val))
        return traverse(root, targetSum)