import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())

        counts = {}
        for w in words:
            if w not in banned_set:
                counts[w] = counts.get(w, 0) + 1

        return max(counts, key=counts.get)