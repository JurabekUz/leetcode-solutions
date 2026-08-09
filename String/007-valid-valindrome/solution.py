

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         result = True
#
#         clean_chars = [i for i in s.lower() if i.isalnum()]
#         i = 0
#         j = len(clean_chars)-1
#         while i <= j:
#             if clean_chars[i] != clean_chars[j]:
#                 result = False
#                 break
#             i += 1
#             j -= 1
#
#         print(result)
#         return result

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         result = True
#         clean_chars = [i for i in s.lower() if i.isalnum()]
#
#         k1 = len(clean_chars) // 2
#         digit = len(clean_chars) % 2
#
#         first_half = clean_chars[0:k1]
#         second_half = clean_chars[k1+digit:]
#         second_half.reverse()
#         if clean_chars and first_half != second_half:
#             result = False
#
#         print(result)
#         return result


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")
sol.isPalindrome("race a car")
sol.isPalindrome(" ")
