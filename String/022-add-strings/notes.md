Pattern:
Two Pointers / Elementary Column Addition (Carry Simulation)

Recognition:
Need to add two non-negative integers represented as strings without:
1. Direct conversion to integer (e.g. `int(num)`).
2. Any built-in BigInteger library.

Core idea:
1. Initialize two pointers `i` and `j` at the end (least significant digit) of each string, with `carry = 0`.
2. Loop while `i >= 0` or `j >= 0` or `carry > 0`:
   - Extract the digit value: `ord(s[k]) - ord('0')` (or 0 if pointer out of bounds).
   - Compute `total = n1 + n2 + carry`.
   - Append `str(total % 10)` to a list `res`.
   - Update `carry = total // 10`.
   - Decrement both pointers.
3. Reverse `res` and join into the final string.

Why append to list instead of string concatenation?
- In Python, `res = str(s) + res` copies the string each iteration, resulting in O(N^2) time.
- Appending to a list and reversing at the end achieves optimal O(N) time.

Complexity:
- Time: O(max(len(num1), len(num2)))
- Space: O(max(len(num1), len(num2))) for the result list