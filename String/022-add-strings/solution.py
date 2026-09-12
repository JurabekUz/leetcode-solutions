class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = n1 + n2 + carry
            res.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return "".join(reversed(res))

sol = Solution()

ans = sol.addStrings("18", "584")
assert ans == "602"

ans = sol.addStrings("11", "157")
assert ans == "168"

ans = sol.addStrings("77", "489")
print(ans)
assert ans == "566"

ans = sol.addStrings("0", "0")
assert ans == "0"

