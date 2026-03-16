class Solution:
    # Iterative
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            adjMap.setdefault(u, []).append(v)
            adjMap.setdefault(v, []).append(u)
        print(adjMap)

        visited = set()

        comp = 0
        for node in range(n):
            if node in visited:
                continue
            comp += 1
            stack = [(-1, node)]

            while stack:
                parent, current = stack.pop()
                if current in visited:  # has cycle
                    continue
                visited.add(current)

                if current in adjMap:
                    for neighbour in adjMap[current]:
                        if neighbour != parent:
                            stack.append((current, neighbour, False))

        return comp
    
    # Recursive
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            adjMap.setdefault(u, []).append(v)
            adjMap.setdefault(v, []).append(u)
        print(adjMap)

        visited = set()

        def dfs(parent, node):
            if node in visited:
                return
            visited.add(node)

            if node in adjMap:
                for neighbour in adjMap[node]:
                    if neighbour != parent:
                        dfs(node, neighbour)
            
            return
        
        comp = 0
        for node in range(n):
            if not node in visited:
                comp += 1
                dfs(-1, node)
        return comp
    
n=5
edges=[[0,1],[1,2],[3,4]]
print(Solution().countComponents(n, edges))
