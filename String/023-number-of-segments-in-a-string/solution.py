class Solution:
    def countSegments(self, s: str) -> int:
        """
        A segment starts when current character is not a space
        and the previous character was a space (or it is the first character).
        """
        count = 0
        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i - 1] == " "):
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()

    # Standard cases
    assert sol.countSegments("Hello, my name is John") == 5
    assert sol.countSegments("Hello") == 1

    # Edge cases: multiple spaces, leading/trailing spaces
    assert sol.countSegments("   foo   bar   ") == 2
    assert sol.countSegments("") == 0
    assert sol.countSegments("                ") == 0

    # Edge cases: punctuation counts as segments
    assert sol.countSegments(", , , ,        a, eaefa") == 6
    assert (
        sol.countSegments(
            "Of all the gin joints in all the towns in all the world,   "
        )
        == 13
    )

    print("All test cases passed!")
