class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # def in_order_traversal(self, current_p, current_q):
    #     def nodes_equal(a, b):
    #         if (a is None) != (b is None):
    #             return False
    #         if a and b and a.val != b.val:
    #             return False
    #         return True

    #     if current_p is None and current_q is None:
    #         return
    #     if not nodes_equal(current_p, current_q):
    #         raise(Exception)
    #     self.in_order_traversal(current_p.left, current_q.left)
    #     self.in_order_traversal(current_p.right, current_q.right)

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     try:
    #         self.in_order_traversal(p, q)
    #     except (Exception):
    #         return False
    #     return True

    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if (not root and subRoot) or (not subRoot and root):
    #         return False
    #     if self.isSameTree(root, subRoot):
    #         return True
    #     return (
    #         self.isSubtree(root.left, subRoot) or
    #         self.isSubtree(root.right, subRoot)
    #     )

    rootStr = ""
    subRootStr = ""

    def pre_order_traversal(self, root: Node, isRoot: bool):
        if root is None:
            if isRoot:
                self.rootStr += "yxy"
            else:
                self.subRootStr += "yxy"
            return
        if isRoot:
            self.rootStr += f"y{str(root.val)}y"
        else:
            self.subRootStr += f"y{str(root.val)}y"
        self.pre_order_traversal(root.left, isRoot)
        self.pre_order_traversal(root.right, isRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.rootStr = ""
        self.subRootStr = ""
        self.pre_order_traversal(root, True)
        self.pre_order_traversal(subRoot, False)
        print(self.rootStr)
        print(self.subRootStr)
        if self.subRootStr in self.rootStr:
            return True
        return False


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
