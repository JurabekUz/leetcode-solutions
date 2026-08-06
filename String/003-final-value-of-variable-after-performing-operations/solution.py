from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ks = {
            "++X" : 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }
        total = 0
        for i in operations:
            total += ks[i]
        return total