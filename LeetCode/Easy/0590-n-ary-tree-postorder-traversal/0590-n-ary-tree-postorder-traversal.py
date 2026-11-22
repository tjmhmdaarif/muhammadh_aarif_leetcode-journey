"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            curr = stack.pop()
            result.append(curr.val)

            if curr.children:
                stack.extend(curr.children)

        return result[::-1]
        