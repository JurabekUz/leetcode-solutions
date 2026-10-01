class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing_numbers = list(range(len(nums)+1)) - nums
        return missing_numbers[0]

    #other solution
    """
    result = len(nums)

    for i, num in enumerate(nums):
        result ^= i ^ num

    return result
    """