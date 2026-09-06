Pattern:
Two Pointers (Greedy Matching)

Recognition:
Need to check if all characters of string `s` appear in string `t` in the exact same relative order.
Frequency counter / ASCII / Set does not work because order matters (e.g., s="axc", t="ahbgdc").

Core idea:
1. Use two pointers: `i` for `s` (target) and `j` for `t` (source).
2. Pointer `j` always advances through `t`.
3. Pointer `i` advances only when `s[i] == t[j]`.
4. If `i == len(s)`, all characters in `s` have been found in order -> return True.
5. If the loop ends before `i == len(s)` -> return False.

Complexity:
- Time: O(len(t))
- Space: O(1)