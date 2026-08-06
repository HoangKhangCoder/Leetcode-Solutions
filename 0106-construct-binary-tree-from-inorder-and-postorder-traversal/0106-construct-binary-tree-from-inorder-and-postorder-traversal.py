# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode()
        index = {x: i for i, x in enumerate(inorder)}
        def helper(left, right):
            if left > right:
                return None
            val = postorder.pop()
            idx = index[val]
            root = TreeNode(val)
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            return root
            
        return helper(0, len(inorder) - 1)