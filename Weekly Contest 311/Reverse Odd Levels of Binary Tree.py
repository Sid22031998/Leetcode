# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def getElements(root, level):
            if root is None:
                return
            if level in drr:
                drr[level].append(root.val)
            else:
                drr[level]=[root.val]
            getElements(root.left, level+1)
            getElements(root.right, level+1)
            return
        
        def modifyTree(root, level):
            if root is None:
                return None
            if level%2!=0:
                root.val=drr[level].pop()
            modifyTree(root.left, level+1)
            modifyTree(root.right, level+1)
            return 
        
        drr={}
        getElements(root, 0)
        modifyTree(root, 0)
        return root
