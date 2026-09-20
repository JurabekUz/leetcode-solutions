class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        start = 0
        ans = []
        l = s[0]
        for i in range(len(s)):
            if s[i] != l:
                if i-start >= 3:
                    ans.append([start, i-1])
                l = s[i]
                start = i
            elif len(s) == i+1 and i-start >= 2:
                ans.append([start, i])
        return ans
