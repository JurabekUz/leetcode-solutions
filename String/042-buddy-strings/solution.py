class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # 1. Must have identical lengths
        if len(s) != len(goal):
            return False

        # 2. If strings are already equal, check for at least one duplicate character
        if s == goal:
            return len(set(s)) < len(s)

        # 3. Find all mismatched indices
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2:  # More than 2 differences can never be fixed in 1 swap
                    return False

        # 4. Exactly 2 mismatches that can be swapped
        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]