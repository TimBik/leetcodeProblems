from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.path = []
        self.paths = []
        self.rec(root)
        return self.paths

    def rec(self, root):
        if root is None:
            return
        self.path.append(str(root.val))
        if root.left is None and root.right is None:
            self.paths.append("->".join(self.path) if len(self.path) > 1 else str(self.path[0]))
        self.rec(root.left)
        self.rec(root.right)
        self.path.pop()
        return self.paths


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.right = TreeNode(5)
Solution().binaryTreePaths(head)
