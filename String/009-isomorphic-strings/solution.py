class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matching = {}

        for i in range(len(s)):
            if s[i] in matching:
                if matching[s[i]] != t[i]:
                    return False
            elif t[i] in matching.values():
                return False
            else:
                matching[s[i]] = t[i]

        return True