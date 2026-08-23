# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Idea: the last element of postorder is always the root of the
        # current tree (or subtree). Using the root's position in inorder,
        # we know which range belongs to the left subtree and which belongs
        # to the right subtree. Since postorder has the form
        # [left, right, root], when we pop() from the end we must build the
        # right subtree first, then the left subtree, so the pop() order
        # lines up correctly.
        index = {x: i for i, x in enumerate(inorder)}  # fast lookup of a value's position in inorder

        def helper(left, right):
            # left, right: the left/right index bounds in the inorder array for the subtree being built
            if left > right:
                return None
            val = postorder.pop()   # the last element of postorder is the root of the current subtree
            idx = index[val]        # the root's position in inorder
            root = TreeNode(val)
            # Build the right subtree first because postorder.pop() takes
            # from the end, and the next element from the end belongs to
            # the right subtree
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            return root

        return helper(0, len(inorder) - 1)