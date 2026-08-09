
# 1
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#
#         i = len(a)-1
#         j = len(b)-1
#         carry = 0
#         result = ''
#         while i >=0 or j >= 0:
#             if i >=0:
#                 i_num = int(a[i])
#             else:
#                 i_num = 0
#
#             if j >=0:
#                 j_num = int(b[j])
#             else:
#                 j_num = 0
#
#             s = i_num + j_num + carry
#             if s == 2:
#                 carry = 1
#                 result = "0" + result
#             elif s == 3:
#                 carry = 1
#                 result = "1" + result
#             else:
#                 result = str(s) + result
#
#             i-=1
#             j-=1
#
#         if carry == 1:
#             result = "1" + result
#
#         print(result)
#         return result

# 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0:
            i_num = int(a[i]) if i >= 0 else 0
            j_num = int(b[j]) if j >= 0 else 0

            total = i_num + j_num + carry

            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        if carry:
            result.append("1")

        return "".join(reversed(result))

sol = Solution()
sol.addBinary("1110", "101")
sol.addBinary("110", "101000")
sol.addBinary("110", "101")
sol.addBinary("11", "10")
sol.addBinary("11", "11")
sol.addBinary("0", "1")
sol.addBinary("1", "1")
sol.addBinary("0", "0")
