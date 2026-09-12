# 434. Number of Segments in a String

## Problem
Given a string `s`, return the number of segments in the string.
A **segment** is defined to be a contiguous sequence of non-space characters.

---

## Pattern: Segment Boundary Detection (In-Place State Scan)

Instead of splitting the string into substrings or allocating new arrays in memory, detect the **beginning of each new segment** while scanning linearly.

### Recognition:
- A new segment starts at index `i` if and only if:
  1. The current character is **not a space**: `s[i] != ' '`
  2. **AND** it is either the very first character of the string (`i == 0`) OR the preceding character was a space (`s[i - 1] == ' '`).

```text
Index:   0   1   2   3   4   5   6   7   8   9  10  11
s:     ' ' ' ' 'H' 'i' ' ' ' ' 't' 'h' 'e' 'r' 'e' ' '
i=2:    s[2]='H' (non-space) and s[1]=' ' (prev is space) -> START of segment 1
i=6:    s[6]='t' (non-space) and s[5]=' ' (prev is space) -> START of segment 2
Total Segments = 2
```

---

## Optimal Algorithm

```python
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i - 1] == " "):
                count += 1
        return count
```

### Alternative (Pythonic):
```python
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
```
*Note: `s.split()` with no arguments splits by consecutive whitespace runs and discards leading/trailing whitespace.*

---

## Complexity

- **Time Complexity**: $\mathcal{O}(n)$ — Single linear pass through string `s` of length $n$.
- **Space Complexity**:
  - **In-place scan**: $\mathcal{O}(1)$ auxiliary space — uses only a single integer counter.
  - **`s.split()`**: $\mathcal{O}(n)$ auxiliary space — allocates a list containing copies of all segment strings.

---

## Pitfalls & Wrong Approaches

### ❌ 1. `s.split(' ')` with explicit space delimiter
- **Mistake**: Calling `len(s.split(' '))` instead of `len(s.split())`.
- **Why it fails**: Passing `' '` explicitly treats *each single space* as a separator, producing empty strings `""` between consecutive spaces and for leading/trailing spaces:
  - `s = "a   b"` $\to$ `s.split(' ')` gives `['a', '', '', 'b']` $\to$ length `4` (Expected `2`).
  - `s = ""` $\to$ `"".split(' ')` gives `[""]` $\to$ length `1` (Expected `0`).
  - `s = "   "` $\to$ `"   ".split(' ')` gives `['', '', '', '']` $\to$ length `4` (Expected `0`).

### ❌ 2. Counting Spaces: `s.count(' ') + 1`
- **Mistake**: Assuming words = number of spaces + 1.
- **Why it fails**:
  - `s = ""` $\to$ `0 + 1 = 1` (Expected `0`).
  - `s = "   "` $\to$ `3 + 1 = 4` (Expected `0`).
  - `s = "   hello   "` $\to$ `6 + 1 = 7` (Expected `1`).
  - Sentences with multiple spaces between words will severely overcount segments.

### ❌ 3. Forgetting Boundary Check & Python Negative Indexing (`s[-1]`)
- **Mistake**: Writing `if s[i] != ' ' and s[i - 1] == ' ':` without checking `i == 0`.
- **Why it fails**: In Python, when `i = 0`, `s[i - 1]` evaluates to `s[-1]` (the last character of the string).
  - If `s = "hello"`: `s[0] = 'h'` and `s[-1] = 'o' != ' '`, so the first segment is never counted!
  - Always guard with `(i == 0 or s[i - 1] == ' ')`.

### ❌ 4. Assuming Segments Only Contain Letters or Alphanumerics
- **Mistake**: Using regex `re.findall(r'\w+', s)` or filtering characters with `s[i].isalnum()`.
- **Why it fails**: A segment is defined as *any contiguous non-space characters*, including punctuation and symbols.
  - Example: `s = ", , , ,        a, eaefa"`
  - Segments are `[",", ",", ",", ",", "a,", "eaefa"]` (Total = `6`).
  - Punctuation strings like `","` are valid segments.
