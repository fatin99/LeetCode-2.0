# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Iterative post-order traversal
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack = [(root, root.val)]
        max_diameter = None
        node_heights = {None: 0}

        while stack:
            node, path_sum = stack[-1]

            if node.left and node.left not in node_heights:
                stack.append((node.left, path_sum + node.left.val))
            elif node.right and node.right not in node_heights:
                stack.append((node.right, path_sum + node.right.val))

            else:
                stack.pop()
                left_height = node_heights[node.left]
                right_height = node_heights[node.right]
                curr_height = node.val + max(left_height, right_height)
                node_heights[node] = max(curr_height, node.val)

                diameter = node.val
                if left_height >= 0:
                    diameter += left_height
                if right_height >= 0:
                    diameter += right_height
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
