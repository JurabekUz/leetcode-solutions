
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        available = Counter(magazine)

        for char in ransomNote:
            if available[char] == 0:
                return False
            available[char] -= 1

        return True