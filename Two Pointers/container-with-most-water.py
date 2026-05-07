class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0
        while start < end:
            length = end - start
            leftHeight = height[start]
            rightHeight = height[end]
            currHeight = min(leftHeight, rightHeight)
            area = max(area, currHeight * length)
            if leftHeight < rightHeight:
                start += 1
            else:
                end -= 1
        return area


print(Solution().maxArea([1, 1]))
