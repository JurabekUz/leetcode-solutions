class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total = 0
        max_i = len(timeSeries)-1
        for i in range(max_i+1):
            if i == max_i:
                total += duration
            else:
                diff = timeSeries[i+1] - timeSeries[i]
                total += min(diff, duration)
        return total