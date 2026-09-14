class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Algorithm 1 (Greedy Two Pointers with Slicing):
        Scan from both ends with two pointers.
        At the first mismatch s[left] != s[right], we can delete at most one character:
        - either delete s[left]: check if s[left + 1 : right + 1] is a palindrome
        - or delete s[right]: check if s[left : right] is a palindrome
        Time: O(N), Space: O(N) due to slicing
        """
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skip_left = s[left + 1 : right + 1]
                skip_right = s[left : right]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            left += 1
            right -= 1

        return True

    def validPalindromeTwoPointers(self, s: str) -> bool:
        """
        Algorithm 2 (Pure Two Pointers - In-Place O(1) Space):
        Uses a helper function to check whether a range [l, r] is a palindrome.
        Avoids string slicing and memory allocations.
        Time: O(N), Space: O(1)
        """
        def is_palindrome_range(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("racecar", True),
        ("deeee", True),
        ("eeeed", True),
        ("cabbac", True),
        ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True),
    ]

    for s, expected in test_cases:
        assert sol.validPalindrome(s) == expected, f"Failed on {s}"
        assert sol.validPalindromeTwoPointers(s) == expected, f"Failed on two pointers {s}"

    print("All test cases passed!")
