from collections import defaultdict
from typing import List


class Solution:
    # Iterative
    # Time: O(V + E) | Space: O(V + E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {}
        for prereq in prerequisites:
            if prereq[0] in prereqMap:
                prereqMap[prereq[0]].append(prereq[1])
            else:
                prereqMap[prereq[0]] = [prereq[1]]

        print(prereqMap)

        visited = set()  # nodes that have already been explored
        visiting = (
            set()
        )  # necessary for directed graph, nodes that we are exploring in dfs

        for course in range(numCourses):
            if course in visited:
                continue
            stack = [(course, False)]

            while stack:
                current, explored = stack.pop()
                if explored:
                    visiting.remove(current)
                    visited.add(current)
                    continue

                if current in visiting:  # has cycle
                    print(current)
                    return False
                if current in visited:  # node has already been explored
                    continue

                visiting.add(current)
                stack.append((current, True))

                if current in prereqMap:
                    for prereq in prereqMap[current]:
                        stack.append((prereq, False))

        return True

    # Recursive
    # Time: O(V + E) | Space: O(V + E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {}
        for prereq in prerequisites:
            if prereq[0] in prereqMap:
                prereqMap[prereq[0]].append(prereq[1])
            else:
                prereqMap[prereq[0]] = [prereq[1]]

        print(prereqMap)

        visited = set()
        visiting = set()  # this is needed for undirected graph

        def has_cycle_dfs(current):
            if current in visiting:
                return True
            if current in visited:
                return False

            visiting.add(current)
            if current in prereqMap:
                for prereq in prereqMap[current]:
                    if has_cycle_dfs(prereq):
                        return True
            visiting.remove(current)
            visited.add(current)
            return False

        for course in range(numCourses):
            if course not in visited:
                if has_cycle_dfs(course):
                    return False
        return True


numCourses = 8
prerequisites = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
print(Solution().canFinish(numCourses, prerequisites))
numCourses = 7
prerequisites = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
print(Solution().canFinish(numCourses, prerequisites))
numCourses = 5
prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
print(Solution().canFinish(numCourses, prerequisites))
numCourses = 3
prerequisites = [[1, 0], [1, 2], [0, 1]]
print(Solution().canFinish(numCourses, prerequisites))
numCourses = 20
prerequisites = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
print(Solution().canFinish(numCourses, prerequisites))
numCourses = 3
prerequisites = [[1, 0], [0, 2], [2, 1]]
print(Solution().canFinish(numCourses, prerequisites))
