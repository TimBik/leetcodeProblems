from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None: return ans
        queue = [root, ]
        end_level = 0
        node_id = 0
        while (node_id < len(queue)):
            node = queue[node_id]
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if end_level == node_id:
                ans.append(node.val)
                end_level = len(queue) - 1
            node_id += 1
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(Solution().rightSideView(root))