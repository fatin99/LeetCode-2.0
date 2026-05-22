# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Iterative post-order traversal
    # O(n) time and O(n) space
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        max_diameter = None
        node_heights = {None: 0}

        while stack:
            node = stack[-1]

            if node.left and node.left not in node_heights:
                stack.append(node.left)
            elif node.right and node.right not in node_heights:
                stack.append(node.right)

            else:
                stack.pop()
                left_height = max(node_heights[node.left], 0)
                right_height = max(node_heights[node.right], 0)
                node_heights[node] = node.val + max(left_height, right_height)

                diameter = node.val + left_height + right_height
                if max_diameter == None:
                    max_diameter = diameter
                max_diameter = max(diameter, max_diameter)

        return max_diameter


def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


root = to_binary_tree([1, 2, 3])
print(Solution().maxPathSum(root))
root = to_binary_tree([-10, 9, 20, None, None, 15, 7])
print(Solution().maxPathSum(root))
root = to_binary_tree([2, -1])
print(Solution().maxPathSum(root))
root = to_binary_tree([1, -2, 3])
print(Solution().maxPathSum(root))
root = to_binary_tree([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])
print(Solution().maxPathSum(root))
root = to_binary_tree([-2, 0, 0])
print(Solution().maxPathSum(root))
