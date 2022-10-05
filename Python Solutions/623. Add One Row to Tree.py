# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def helper(root, level):
            if root is None:
                return 
            if level+1==depth:
                left=root.left
                right=root.right
                root.left=TreeNode(val, left=left)
                root.right=TreeNode(val, right=right)
            helper(root.left, level+1)
            helper(root.right, level+1)
            return
        if depth==1:
            return TreeNode(val, left=root)
        helper(root, 1)
        return root
