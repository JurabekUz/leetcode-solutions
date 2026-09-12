# 459. Repeated Substring Pattern

## Problem
Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

---

## Algorithm 1: Prefix Divisor Check (Intuitive & Optimal in Practice)

### Core Idea:
1. A valid repeated substring must appear at least 2 times, so its length `l` can range at most from `1` to `len(s) // 2`.
2. A substring of length `l` can only tile `s` if `len(s)` is evenly divisible by `l` (`len(s) % l == 0`).
3. For each valid divisor `l`, extract `sub = s[:l]` and test if repeating it `n // l` times equals `s`:
   ```python
   if sub * (n // l) == s:
       return True
   ```
4. If no divisor length satisfies this, return `False`.

### Complexity:
- **Time**: $\mathcal{O}(n \times d(n))$, where $d(n)$ is the number of divisors of $n$. For $n \le 10^4$, the maximum number of divisors is $64$.
  Worst-case operations $\approx 64 \times 10^4 \approx 6.4 \times 10^5$ (completes in ~10–20ms).
- **Space**: $\mathcal{O}(n)$ to generate the candidate multiplied string.

---

## Algorithm 2: The String Doubling Trick (One-Liner)

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
```

### Why it works:
1. Let $s$ be composed of repeating block $P$ repeated $k$ times ($k \ge 2$):
   $$s = P_1 P_2 \dots P_k$$
2. Doubling $s$ creates $2k$ copies of $P$:
   $$s + s = P_1 P_2 \dots P_k P_{k+1} \dots P_{2k}$$
3. Slicing `[1:-1]` removes the first character of the first block $P_1$ and the last character of the last block $P_{2k}$.
   - This destroys the trivial instance of $s$ at index $0$.
   - This destroys the trivial instance of $s$ ending at index $2n - 1$.
4. However, the internal copies of $s$ starting at offset $|P|, 2|P|, \dots, (k-1)|P|$ remain completely intact!
5. If $s$ does **not** consist of repeated substrings, the only copies of $s$ in $s + s$ were the two trivial ones at index $0$ and index $n$. Destroying their outer boundaries leaves no complete instance of $s$ inside `(s + s)[1:-1]`.

### Complexity:
- **Time**: $\mathcal{O}(n)$ (standard substring search algorithm in Python).
- **Space**: $\mathcal{O}(n)$ for the concatenated string.

---

## Algorithm 3: KMP (Knuth-Morris-Pratt) LPS Array

- Construct the Longest Proper Prefix which is also Suffix (LPS) array for $s$.
- Let $L = \text{lps}[-1]$ (the length of the longest border).
- If $L > 0$ and $n \pmod{n - L} == 0$, the string is periodic with smallest period $n - L$.
- **Time**: $\mathcal{O}(n)$, **Space**: $\mathcal{O}(n)$.

---

## Pitfalls & Gotchas

1. **Checking non-divisors**:
   - Attempting to check all lengths from $1$ to $n // 2$ without `if n % l == 0:` leads to redundant string multiplications and $\mathcal{O}(n^2)$ time.
2. **Forgetting `[1:-1]` in the Doubling Trick**:
   - `s in (s + s)` is **always True** for every string because $s$ is always present at index $0$ and index $n$. Dropping the first and last characters is mandatory to eliminate these trivial matches.
3. **Upper Bound**:
   - Looping beyond `n // 2` is invalid because a repeated substring must fit into `s` at least twice.
