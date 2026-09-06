from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        even_sum = sum((count // 2) * 2 for count in counts.values())

        return even_sum + 1 if even_sum < len(s) else even_sum
