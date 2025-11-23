# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        def level(i: int, tree):
            if not tree:
                return 
            if len(levels) <= i:
                levels.append([])
            levels[i].append(tree.val)
            
            level(i + 1, tree.left)
            level(i + 1, tree.right)
        level(0, root)
        return levels