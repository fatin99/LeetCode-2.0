# Time:  O(n) — single pass to group, then O(k) over distinct types (k <= n)
# Space: O(k) — two dicts keyed by task type (k = number of distinct types)
from collections import defaultdict


class Solution:
    def analyze(self, task_memory: List[int], task_type: List[int]) -> (int, int, int):
        # Same-type tasks run concurrently in 1 time unit; their memories sum.
        memory_by_type = defaultdict(int)
        for i in range(len(task_memory)):
            memory_by_type[task_type[i]] += task_memory[i]

        # Part 1: peak concurrent memory = heaviest type group.
        max_memory = max(memory_by_type.values())

        # Part 2: under that memory budget every type fits as one batch,
        # so shortest time = number of distinct types.
        shortest_time = len(memory_by_type)

        # Part 3: max concurrency = largest type group's task count.
        count_by_type = defaultdict(int)
        for i in range(len(task_type)):
            count_by_type[task_type[i]] += 1

        max_concurrent = max(count_by_type.values())

        return max_memory, shortest_time, max_concurrent
