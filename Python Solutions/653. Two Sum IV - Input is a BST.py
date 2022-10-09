# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sum_dict={}
        def helper(root):
            if root is None:
                return False
            if k-root.val in sum_dict:
                return True
            sum_dict[root.val]=1
            if helper(root.left) or helper(root.right):
                return True
            return False
        ans=helper(root)
        # print(sum_dict)
        return ans
