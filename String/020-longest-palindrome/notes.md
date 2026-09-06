Pattern:
Frequency Counter / Branchless Arithmetic (Greedy Pairing)

Recognition:
Need to build the longest palindrome from the characters of string `s`.
A palindrome is symmetric:
- Every character must be paired on both sides (left & right).
- At most ONE character can sit in the exact middle with an odd count.

Core idea:
1. Count the frequency of each character using `Counter`.
2. For each character count `c`, extract its largest even part: `(c // 2) * 2`.
3. Sum all the even parts into `even_sum`.
4. If `even_sum < len(s)` (at least one leftover character exists), place one in the middle: return `even_sum + 1`.
5. Otherwise, return `even_sum`.

Complexity:
- Time: O(n)
- Space: O(1) (at most 52 unique uppercase & lowercase letters)