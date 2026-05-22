# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:
    # level order traversal
    # O(n) time for BFS
    # O(n) space length of queue and string
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        # res = ""
        # Python strings are immutable
        # each concatenation (res += "X") copies the entire string -> extra O(n) -> O(n^2)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                # res += str(node.val)
                res.append(str(node.val))
                for child in ("left", "right"):
                    child_node = getattr(node, child)
                    queue.append(child_node)
            else:
                # res += "X"
                res.append("X")
            # res += " "
        # return res
        return " ".join(res)

    # O(n) time
    # O(n) space
    def deserialize(self, data):
        if not data:
            return None
        data = data.split()  # O(n) time and space
        if data[0] == "X":
            return None
        root = TreeNode(data[0])  # O(n) space
        queue = deque([root])  # O(n) space

        count = 0
        while queue and count < len(data):  # O(n) time
            node = queue.popleft()
            for child in ("left", "right"):  # O(1)
                count += 1
                if count >= len(data):
                    return root
                if data[count] != "X":
                    child_node = TreeNode(data[count])
                    setattr(node, child, child_node)
                    queue.append(child_node)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
