class Solution:
    # recursive
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(currSum: int, currNums: List[int], index: int) -> None:
            if currSum == target:
                res.append(list(currNums))
                return
            while index < len(candidates):
                num = candidates[index]
                newSum = currSum + num
                if newSum > target:
                    index += 1
                    continue
                currNums.append(num)
                dfs(newSum, currNums, index)
                currNums.pop()
                index += 1

        dfs(0, [], 0)
        return res

    # iterative
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = [(0, [], 0)]

        while stack:
            currSum, currNums, index = stack.pop()

            if currSum == target:
                res.append(list(currNums))
                continue

            while index < len(candidates):
                num = candidates[index]
                newSum = currSum + num
                if newSum > target:
                    index += 1
                    continue
                currNums.append(num)
                stack.append((newSum, currNums + [num], index))
                index += 1
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
