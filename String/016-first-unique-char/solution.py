class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        connts = Counter(s)

        for i in range(len(s)):
            if connts[s[i]] == 1:
                return i
        return -1