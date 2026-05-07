# Time:  O(n log n) — sorting dominates; the assignment pass is O(n)
# Space: O(n) — sorted index list, leftover queue, and result array
class Solution:
    def maxAdvantageSum(self, a: List[int], b: List[int]) -> (int, List[int]):
        n = len(a)
        b_sorted = sorted(b)

        # Build (value, index) pairs for a, then sort by value to walk a in ascending order.
        a_indexed = []
        for i in range(n):
            a_indexed.append((a[i], i))
        a_indexed.sort()

        result = [0] * n
        leftover = []
        j = 0
        total = 0

        # Greedy: for each a in ascending order, use smallest b that still beats it.
        # Saves larger b's for larger a's, maximizing # of wins -> max sum of winners.
        for pair in a_indexed:
            i = pair[1]
            if j < n and b_sorted[j] > a[i]:
                result[i] = b_sorted[j]
                total += b_sorted[j]
                j += 1
            else:
                leftover.append(i)

        # Place remaining (losing) b's into the unmatched positions.
        for i in leftover:
            result[i] = b_sorted[j]
            j += 1

        return total, result

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_sorted = sorted(nums1)
        nums2_sorted = []
        for i in range(len(nums2)):
            nums2_sorted.append((nums2[i], i))
        nums2_sorted.sort()

        res = [-1] * len(nums1)
        leftover = []
        total = 0

        j = 0
        for num1 in nums1_sorted:
            i = nums2_sorted[j][1]
            num2 = nums2_sorted[j][0]

            if j < len(nums1) and num1 > num2:
                res[i] = num1
                j += 1
                total += num1
            else:
                leftover.append(num1)

        for i in range(len(res)):
            if res[i] == -1:
                res[i] = leftover.pop()

        return total, res


# nums1 = [2,7,11,15]
# nums2 = [1,10,4,11]
# print(Solution().advantageCount(nums1, nums2))
# print(Solution().maxAdvantageSum(nums2, nums1))

nums1 = [12, 24, 8, 32]
nums2 = [13, 25, 32, 11]
print(Solution().advantageCount(nums1, nums2))
print(Solution().maxAdvantageSum(nums2, nums1))
