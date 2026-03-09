class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        if root:
            queue.append((root, []))
        while queue:
            for _ in range(len(queue)):
                node, path = queue.popleft()
                if node.left:
                    if node.val <= node.left.val:
                        return False
                    queue.append((node.left, path + [(node, True, False)]))
                if node.right:
                    if node.val >= node.right.val:
                        return False
                    queue.append((node.right, path + [(node, False, True)])) 
                for ancestor in path:
                    parent = ancestor[0]
                    left = ancestor[1]
                    right = ancestor[2]
                    if left:
                        if node.val >= parent.val:
                            return False
                    if right:
                        if node.val <= parent.val:
                            return False
        return True

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

root = to_binary_tree([5,4,6,None,None,3,7])
print(Solution().isValidBST(root))

root = to_binary_tree([3,1,5,0,2,4,6])
print(Solution().isValidBST(root))
