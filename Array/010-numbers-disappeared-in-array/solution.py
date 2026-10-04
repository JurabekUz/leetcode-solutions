class Solution:

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])

        return [
            i + 1
            for i in range(len(nums))
            if nums[i] > 0
        ]