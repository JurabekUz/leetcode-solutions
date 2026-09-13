# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         if word.islower() or word.isupper():
#             return True
#         if word.istitle() and word[1:].islower():
#             return True
#         return False

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = sum(c.isupper() for c in word)

        # Valid if:
        # 1. All letters are caps (caps == len(word))
        # 2. No letters are caps (caps == 0)
        # 3. Exactly one cap and it's at index 0 (caps == 1 and word[0].isupper())
        return caps == len(word) or caps == 0 or (caps == 1 and word[0].isupper())