class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if candidate == None:
                candidate = num
                count =1
            elif num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = None

        return candidate
