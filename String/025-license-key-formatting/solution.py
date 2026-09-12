class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        Algorithm 1 (Remainder Calculation & Forward Slicing):
        1. Remove all dashes and convert lowercase to uppercase.
        2. If the cleaned string is empty, return "".
        3. The first group size is len(clean) % k (or k if remainder is 0).
        4. Append the first group, then slice remaining groups of size k.
        Time: O(N), Space: O(N)
        """
        clean = s.replace("-", "").upper()
        if not clean:
            return ""

        first_len = len(clean) % k or k
        res = [clean[:first_len]]

        for i in range(first_len, len(clean), k):
            res.append(clean[i : i + k])

        return "-".join(res)

    def licenseKeyFormattingReversed(self, s: str, k: int) -> str:
        """
        Algorithm 2 (Reverse Chunking):
        Since groups of size k are formed from right to left,
        reverse the cleaned string, chunk in slices of k, join with '-',
        and reverse the whole formatted string back.
        Time: O(N), Space: O(N)
        """
        clean = s.replace("-", "").upper()
        rev = clean[::-1]
        chunks = [rev[i : i + k] for i in range(0, len(rev), k)]
        return "-".join(chunks)[::-1]


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("5F3Z-2e-9-w", 4, "5F3Z-2E9W"),
        ("2-5g-3-J", 2, "2-5G-3J"),
        ("2-4A0r7-4k", 4, "24A0-R74K"),
        ("---", 3, ""),
        ("r", 1, "R"),
        ("a-a-a-a-", 1, "A-A-A-A"),
        ("--a-a-a-a--", 2, "AA-AA"),
        ("aaaa", 2, "AA-AA"),
    ]

    for s, k, expected in test_cases:
        assert sol.licenseKeyFormatting(s, k) == expected, f"Failed on {s}, {k}"
        assert sol.licenseKeyFormattingReversed(s, k) == expected, f"Failed reversed on {s}, {k}"

    print("All test cases passed!")
