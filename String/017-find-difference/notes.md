## 389. Find the Difference

### Intuition:
- A `set` cannot handle duplicates (e.g., `s = "a"`, `t = "aa"`).
- We can use Bitwise XOR (`^`) because `x ^ x = 0` and `x ^ 0 = x`.
- Every matching character cancels out, leaving only the unique extra character.

### Algorithm:
1. Initialize `res = 0`.
2. XOR the ASCII value of each character in `s` and `t` into `res`.
3. Convert `res` back to a character via `chr(res)`.

### Complexity:
- **Time**: O(N)
- **Space**: O(1)