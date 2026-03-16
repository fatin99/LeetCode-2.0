class Solution:
    # Iterative
    # Time: O(V + E) | Space: O(V + E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adjMap = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            adjMap.setdefault(u, []).append(v)
            adjMap.setdefault(v, []).append(u)
        print(adjMap)
            
        visited = set()
        stack = [(0, -1)]
        while stack:
            current, parent = stack.pop()
            if current in visited: # has cycle
                return False
            visited.add(current)

            if current in adjMap:
                for neighbour in adjMap[current]:
                    if neighbour != parent:
                        stack.append((neighbour, current))            

        if len(visited) < n:
            return False
        
        return True
    
    # Recursive
    # Time: O(V + E) | Space: O(V + E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adjMap = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            adjMap.setdefault(u, []).append(v)
            adjMap.setdefault(v, []).append(u)
        print(adjMap)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            if node in adjMap:
                for neighbour in adjMap[node]:
                    if neighbour != parent:
                        if not dfs(neighbour, node):
                            return False
            
            return True
            
        if not dfs(0, -1):
            return False
        if len(visited) < n:
            return False
        
        return True
    
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(Solution().validTree(n, edges))
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(Solution().validTree(n, edges))
n=5
edges=[[0,1],[2,0],[3,0],[1,4]]
print(Solution().validTree(n, edges))
