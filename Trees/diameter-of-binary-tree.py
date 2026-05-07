class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_diameter = 0

    # def pre_order_traversal(self, node):
    #     if node is None:
    #         return 0
    #     left_height = self.pre_order_traversal(node.left)
    #     right_height = self.pre_order_traversal(node.right)
    #     self.max_diameter = max(self.max_diameter, left_height+right_height)
    #     return 1 + max(left_height, right_height)

    # Iterative DFS
    node_heights = {}

    def pre_order_traversal(self, node):
        stack = [node]
        self.node_heights = {None: 0}
        maxDiameter = 0

        while stack:
            node = stack[-1]

            if node.left and node.left not in self.node_heights:
                stack.append(node.left)
            elif node.right and node.right not in self.node_heights:
                stack.append(node.right)
            else:
                node = stack.pop()
                print(f"node: {node.val if node else None}")
                leftHeight = self.node_heights[node.left]
                rightHeight = self.node_heights[node.right]
                self.node_heights[node] = 1 + max(leftHeight, rightHeight)
                maxDiameter = max(leftHeight + rightHeight, maxDiameter)

        return maxDiameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_height = 0
        self.node_heights = {None: 0}
        # self.pre_order_traversal(root)
        # # for node, (height, diameter) in self.node_heights.items():
        # #     print(f"node: {node.val if node else None}, height: {height}, diameter: {diameter}")
        #     self.max_diameter = max(self.max_diameter, diameter)
        # return self.max_height
        return self.pre_order_traversal(root)


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


# root = to_binary_tree([1,2])
# print(Solution().diameterOfBinaryTree(root))
root = to_binary_tree([1, 2, None, None, 4, 5, 6])
print(Solution().diameterOfBinaryTree(root))
