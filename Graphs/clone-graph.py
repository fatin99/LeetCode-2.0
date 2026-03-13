# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque
class Solution:
    # DFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        stack = []
        newNode = None
        created = {}
        if node:
            newNode = Node(node.val)
            stack.append((node, newNode))
            created[node.val] = newNode

        while stack:
            current, newCurrent = stack.pop()
            for neighbor in current.neighbors:
                if neighbor.val in created:
                    newNeighbor = created[neighbor.val]
                else:
                    newNeighbor = Node(neighbor.val)
                    created[neighbor.val] = newNeighbor
                if not current in visited:
                    newCurrent.neighbors.append(newNeighbor)
                if not neighbor in visited:
                    stack.append((neighbor, newNeighbor))
            if not current in visited:
                visited.add(current)

        return newNode
    
    # BFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        queue = deque()

        newNode = None
        created = {}

        if node: 
            newNode = Node(node.val)
            created[node.val] = newNode
            visited.add(node)
            queue.append((node, newNode))

        while queue:
            current, newCurrent = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor.val in created:
                    newNeighbor = created[neighbor.val]
                else:
                    newNeighbor = Node(neighbor.val)
                    created[neighbor.val] = newNeighbor  
                newCurrent.neighbors.append(newNeighbor)           
                if not neighbor in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, newNeighbor))

        return newNode