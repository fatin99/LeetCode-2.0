class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(currSum: int, currNums: List[int], index: int) -> None:
            if currSum == target:
                res.append(list(currNums))
                return
            while index in range(len(candidates)):
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

print(Solution().combinationSum([2,3,6,7], 7))
