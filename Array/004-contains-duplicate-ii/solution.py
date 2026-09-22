class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}

        for i, num in enumerate(nums):
            if num in d:
                if abs(d[num]-i)<=k:
                    return True
            d[num] = i
        return False


