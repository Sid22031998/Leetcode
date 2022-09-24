class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def helper(root, path):
            if root is None:
                return []
            if root.left is None and root.right is None:
                if sum(path)+root.val==targetSum:
                    path.append(root.val)
                    ans.append(path[:])
                    path.pop()
            helper(root.left, path+[root.val])
            helper(root.right, path+[root.val])
        helper(root, [])
        return ans
