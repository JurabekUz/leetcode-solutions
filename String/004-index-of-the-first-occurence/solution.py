class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)

        if len(haystack) == 1:
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(len(haystack) - length + 1):
            if haystack[i:i + length] == needle:
                return i

        return -1