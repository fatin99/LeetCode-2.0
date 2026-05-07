from logging import root
from xml.dom.minidom import Node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # def pre_order_traversal(root: Node):
    #     if root is not None:
    #         print(root.val)
    #         self.pre_order_traversal(root.left)
    #         self.pre_order_traversal(root.right)

    # def in_order_traversal(self, node, nodes):
    #     if node is None:
    #         return
    #     self.in_order_traversal(node.left, nodes)
    #     nodes.append(node.val)
    #     self.in_order_traversal(node.right, nodes)

    # def post_order_traversal(root: Node):
    #     if root is not None:
    #         self.post_order_traversal(root.left)
    #         self.post_order_traversal(root.right)
    #         print(root.val)

    # def pre_order_traversal(root, nodes):
    #     if root is None:
    #         return
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         nodes.append(node.val)
    #         # Push right first (so left is processed first)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)

    # def in_order_traversal(root, nodes):
    #     stack = []
    #     current = root
    #     while stack or current:
    #         # Go left as far as possible
    #         while current:
    #             stack.append(current)
    #             current = current.left
    #         current = stack.pop()
    #         nodes.append(current.val)
    #         current = current.right

    # def post_order_traversal(root, nodes):
    #     if root is None:
    #         return
    #     stack1 = [root]
    #     stack2 = []
    #     while stack1:
    #         node = stack1.pop()
    #         stack2.append(node)
    #         if node.left:
    #             stack1.append(node.left)
    #         if node.right:
    #             stack1.append(node.right)
    #     while stack2:
    #         nodes.append(stack2.pop().val)

    # def in_order_traversal(self, root_p, root_q):
    #     stack_p, stack_q = [], []
    #     current_p, current_q = root_p, root_q
    #     if not self.nodes_equal(current_p, current_q):
    #         return False

    #     while (stack_p or current_p) and (stack_q or current_q):
    #         # Go left as far as possible
    #         while current_p and current_q:
    #             stack_p.append(current_p)
    #             stack_q.append(current_q)
    #             current_p = current_p.left
    #             current_q = current_q.left
    #             if not self.nodes_equal(current_p, current_q):
    #                 return False

    #         current_p = stack_p.pop()
    #         current_q = stack_q.pop()
    #         if not self.nodes_equal(current_p, current_q):
    #             return False

    #         current_p = current_p.right
    #         current_q = current_q.right
    #         if not self.nodes_equal(current_p, current_q):
    #             return False
    #     return True

    def in_order_traversal(self, current_p, current_q):
        def nodes_equal(a, b):
            if (a is None) != (b is None):
                return False
            if a and b and a.val != b.val:
                return False
            return True

        if current_p is None and current_q is None:
            return
        if not nodes_equal(current_p, current_q):
            raise (Exception)
        self.in_order_traversal(current_p.left, current_q.left)
        self.in_order_traversal(current_p.right, current_q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        try:
            self.in_order_traversal(p, q)
        except Exception:
            return False
        return True

    # BFS
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     q1 = deque([p])
    #     q2 = deque([q])

    #     while q1 and q2:
    #         for _ in range(len(q1)):
    #             nodeP = q1.popleft()
    #             nodeQ = q2.popleft()

    #             if nodeP is None and nodeQ is None:
    #                 continue
    #             if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
    #                 return False

    #             q1.append(nodeP.left)
    #             q1.append(nodeP.right)
    #             q2.append(nodeQ.left)
    #             q2.append(nodeQ.right)

    #     return True


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


p = to_binary_tree([1, 2, 3])
q = to_binary_tree([1, 2, 3])
print(Solution().isSameTree(p, q))
