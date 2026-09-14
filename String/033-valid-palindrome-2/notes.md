# 680. Valid Palindrome II

## Problem
Given a string `s`, return `true` if the `s` can be palindrome after deleting **at most one** character from it.

---

## Why Brute-Force Fails (Time Limit Exceeded - $\mathcal{O}(N^2)$)

### The Mistake:
Trying to simulate deleting each character at index `idx` from $0$ to $N - 1$, then running a two-pointer palindrome check for each deletion:
- Outer loop runs $N$ times.
- Inner check takes $\mathcal{O}(N)$.
- Total Time: $\mathcal{O}(N^2)$.
- For $N = 10^5$, operations $\approx \frac{(10^5)^2}{2} = 5 \times 10^9$, easily hitting **Time Limit Exceeded (TLE)** on LeetCode.

---

## Algorithm 1: Greedy Two Pointers + Slicing ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)

### Core Idea:
1. Initialize two pointers: `left = 0`, `right = len(s) - 1`.
2. As long as `s[left] == s[right]`, these characters are symmetric and match. Greedy choice: keep both characters (`left += 1`, `right -= 1`).
3. **At the first mismatch (`s[left] != s[right]`)**:
   - Because at most 1 character can be deleted, the culprit must be either `s[left]` or `s[right]`.
   - **Case 1**: Delete `s[left]`, test if `s[left + 1 : right + 1]` is a palindrome.
   - **Case 2**: Delete `s[right]`, test if `s[left : right]` is a palindrome.
   - If either is a palindrome, return `True`; otherwise, return `False`.
4. If no mismatch occurs throughout the loop, `s` was already a palindrome $\implies$ `True`.

### Python Implementation:
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skip_l = s[left + 1 : right + 1]
                skip_r = s[left : right]
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            left += 1
            right -= 1

        return True
```

---

## Algorithm 2: Two-Pointer Helper Function ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Auxiliary Space)

In technical interviews, creating slices (`s[left:right]`) allocates new string copies in memory. We can achieve **$\mathcal{O}(1)$ extra memory** by using an in-place range palindrome validator:

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1

        return True
```

---

## Complexity Analysis

| Approach | Time Complexity | Auxiliary Space | LeetCode Status |
| :--- | :--- | :--- | :--- |
| **Brute Force (Delete Every Index)** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | ❌ TLE ($5 \times 10^9$ ops) |
| **Greedy Two Pointers + Slicing** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ (slice copy) | ✅ Accepted (~30ms) |
| **In-Place Two-Pointer Range** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | ✅ Accepted (~25ms) |

---

## Pitfalls & Key Takeaways

1. **Greedy Choice Property**:
   - Matching outer characters never need to be deleted because keeping symmetric pairs is always optimal.
2. **At Most One Mismatch Branch**:
   - You only branch once! When `s[left] != s[right]`, you check two candidates. You do not need recursion beyond depth 1.
