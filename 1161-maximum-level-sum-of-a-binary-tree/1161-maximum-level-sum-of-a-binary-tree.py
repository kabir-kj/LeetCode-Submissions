# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:return 
        q = [root]
        l,ml,ms = 1,1,root.val
        
        while q:
            s = 0
            tempq = []
            while q:
                x = q.pop()
                s+=x.val
                if x.left:tempq.append(x.left)
                if x.right:tempq.append(x.right)
            if s>ms:
                ml = l
                ms = s
            l+=1
            q = tempq
            
        return ml