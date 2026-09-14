# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         groups = ({"U", "D"}, {"R", "L"})
#         moves_re = moves[::-1]
#         for m1, m2 in zip(moves, moves_re):
#             if all({m1, m2} == i for i in groups):
#                 return False
#         return True

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        counts = (Counter(moves))
        if counts.get("U", 0) != counts.get("D", 0):
            return False
        elif counts.get("L", 0) != counts.get("R", 0):
            return False

        return True
