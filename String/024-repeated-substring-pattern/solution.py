class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Algorithm 1 (Prefix Divisor Check):
        Iterate over prefix lengths l from 1 to n // 2.
        If n % l == 0, check if repeating s[:l] by (n // l) equals s.
        Time: O(n * d(n)), Space: O(n)
        """
        n = len(s)
        for l in range(1, n // 2 + 1):
            if n % l == 0:
                sub = s[:l]
                if sub * (n // l) == s:
                    return True
        return False

    def repeatedSubstringPatternDoubling(self, s: str) -> bool:
        """
        Algorithm 2 (The Doubling Trick):
        s has a repeated substring pattern iff s is in (s + s)[1:-1].
        Time: O(n), Space: O(n)
        """
        return s in (s + s)[1:-1]


if __name__ == "__main__":
    sol = Solution()

    # Standard cases
    assert sol.repeatedSubstringPattern("abab") is True
    assert sol.repeatedSubstringPattern("aba") is False
    assert sol.repeatedSubstringPattern("abcabcabcabc") is True
    assert sol.repeatedSubstringPattern("a") is False
    assert sol.repeatedSubstringPattern("ababba") is False

    # Doubling trick verification
    assert sol.repeatedSubstringPatternDoubling("abab") is True
    assert sol.repeatedSubstringPatternDoubling("aba") is False
    assert sol.repeatedSubstringPatternDoubling("abcabcabcabc") is True
    assert sol.repeatedSubstringPatternDoubling("a") is False
    assert sol.repeatedSubstringPatternDoubling("ababba") is False

    print("All test cases passed!")
