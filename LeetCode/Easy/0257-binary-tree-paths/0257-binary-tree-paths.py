# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        
        result = []
        def dfs(node,current_path):
            if not  node:
                return
            if not current_path:
                current_path = str(node.val)
            else:
                current_path = current_path + "->" + str(node.val)

            if not node.left and not node.right:
                result.append(current_path)
                return
            dfs(node.left, current_path)
            dfs(node.right, current_path)

        dfs(root, "")

        return result