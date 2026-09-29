# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root: TreeNode):

            if not root:
                return None

            if p.val < root.val < q.val or q.val < root.val < p.val:
                return root

            if root == p:
                return p

            if root == q:
                return q

            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            
            if p.val < root.val and q.val < root.val:
                return dfs(root.left)

        return dfs(root)
          
            

        