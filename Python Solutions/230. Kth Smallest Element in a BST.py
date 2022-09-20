class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root):
            elements=[]
            if root is None:
                return elements
            elements.append(root.val)
            if root.left:
                elements+=helper(root.left)
            if root.right:
                elements+=helper(root.right)
            return elements
        
        ans=helper(root)
        ans.sort()
        return ans[k-1]
