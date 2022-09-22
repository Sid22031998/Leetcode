class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def populate(root, level):
            if root is None:
                return None
            if level in drr:
                drr[level].append(root)
            else:
                drr[level]=[root]
            populate(root.left, level+1)
            populate(root.right, level+1)
            return
        
        def connectRight(root, level):
            if root is None:
                return None
            if root.val==drr[level][0].val:
                if len(drr[level])>1:
                    root.next=drr[level][1]
                    drr[level].pop(0)
            connectRight(root.left, level+1)
            connectRight(root.right, level+1)
            return
        
        drr={}
        populate(root, 0)           #store nodes level wise
        # print(drr)
        connectRight(root, 0)       #point node to right node
        return root
