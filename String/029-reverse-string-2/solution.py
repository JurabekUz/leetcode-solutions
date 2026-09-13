class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), 2 * k):
            sl = s[i : i + 2 * k]
            res.append(sl[:k][::-1] + sl[k:])
        return ''.join(res)