# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # In-order traversal

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        while stack or current:
            # Go left as far as possible
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                break
            current = current.right
        return current.val
        