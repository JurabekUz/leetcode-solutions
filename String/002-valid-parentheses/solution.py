class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []

        for char in s:
            if char in pairs:
                stack.append(char)
            elif not stack or pairs[stack[-1]] != char:
                return False
            else:
                stack.pop()

        return not stack
