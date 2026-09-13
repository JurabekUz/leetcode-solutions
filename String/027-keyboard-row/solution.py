class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        return [w for w in words if any(set(w.lower()) <= r for r in rows)]
