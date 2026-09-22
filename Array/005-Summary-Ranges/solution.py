class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []

        begins = None
        for i in range(len(nums)-1):
            if begins == None:
                begins = nums[i]
            if nums[i] + 1 != nums[i+1]:
                result.append(f"{begins}->{nums[i]}")
                begins = None



