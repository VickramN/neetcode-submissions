# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = 1
        res = None
        def dfs(root):

            nonlocal cnt, res

            if not root:
                return None

            if cnt > k:
                return
            dfs(root.left)
            
            if cnt == k:
                res = root.val
            cnt += 1

            dfs(root.right)
            
            return res
        return dfs(root)

            

