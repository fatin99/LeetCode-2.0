class Solution:
    # use set to skip duplicates
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        triples = set()
        for i in range(0, len(nums)):
            currNum = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currLeft = nums[left]
                currRight = nums[right]
                currSum = currNum + currLeft + currRight
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    triplet = str(currNum) + str(currLeft) + str(currRight)
                    if triplet not in triples:
                        triples.add(triplet)
                        result.append([currNum, currLeft, currRight])
                    left += 1
                    right -= 1
        return result

    # store previous 3sum to skip duplicates
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        prevNum = None
        for i in range(0, len(nums)):
            currNum = nums[i]
            if currNum == prevNum:
                continue
            left = i + 1
            right = len(nums) - 1
            prevLeft = None
            prevRight = None
            while left < right:
                currLeft = nums[left]
                currRight = nums[right]
                if currLeft == prevLeft:
                    left += 1
                    continue
                if currRight == prevRight:
                    right -= 1
                    continue
                currSum = currNum + currLeft + currRight
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    result.append([currNum, currLeft, currRight])
                    prevNum = currNum
                    prevLeft = currLeft
                    prevRight = currRight
                    left += 1
                    right -= 1
        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 1, 1]))
print(Solution().threeSum([0, 0, 0]))
print(Solution().threeSum([0, 0, 0, 0]))
print(Solution().threeSum([-2, 0, 1, 1, 2]))
print(Solution().threeSum([1, 2, 0, 1, 0, 0, 0, 0]))
