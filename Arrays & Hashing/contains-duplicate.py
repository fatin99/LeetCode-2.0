class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # https://docs.python.org/2/library/sets.html
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    # Onr line solution
    # return len(set(nums)) < len(nums)
