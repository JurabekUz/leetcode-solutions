
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            result = chr(65 + columnNumber % 26) + result
            columnNumber //= 26

        return result


sol = Solution()
print(sol.convertToTitle(900))
