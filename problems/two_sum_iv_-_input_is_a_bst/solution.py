# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        convert = {}
        kinds = set()
        def helper(root):
            if not root:
                return 
            convert[root.val] = convert.get(root.val, 0) + 1
            kinds.add(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        for x in kinds:
            y = k - x
            if y in kinds and (convert[y] > 1 or y != x):
                return True
        return False