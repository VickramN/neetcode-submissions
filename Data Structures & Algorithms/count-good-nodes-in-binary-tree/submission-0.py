# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    nrOfGoodNodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        
        

        maxVal = root.val

        def dfs(root: TreeNode, maxVal: int):
            

            if not root:
                return None

            if root.val >= maxVal:
                self.nrOfGoodNodes += 1
            
            dfs(root.right, max(root.val, maxVal))
            dfs(root.left, max(root.val, maxVal))

            return self.nrOfGoodNodes

        return dfs(root, maxVal)

            