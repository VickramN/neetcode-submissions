# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(root):
            if not root:
                return None
            r = dfs(root.right)
            l = dfs(root.left)
            v = root.val

            return (r, l, v)

        return dfs(p) == dfs(q)            
