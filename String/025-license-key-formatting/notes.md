# 482. License Key Formatting

## Problem
You are given a license key represented as a string `s` that consists of only alphanumeric characters and dashes. The string is separated into $n + 1$ groups by $n$ dashes. You are also given an integer `k`.

We want to reformat the string `s` such that:
- Each group contains exactly `k` characters, except for the first group, which could be shorter than `k` but must contain at least one character.
- A dash `-` must be inserted between two groups.
- All lowercase letters must be converted to uppercase.

Return the reformatted license key.

---

## Algorithm 1: Remainder Calculation & Forward Slicing (Recommended)

### Core Idea:
1. **Sanitize the Input**: Remove all existing dashes (`s.replace('-', '')`) and convert to uppercase (`.upper()`).
2. **Edge Case**: If the cleaned string is empty (e.g. `s = "---"`), return `""`.
3. **First Group Size**:
   - Because all groups except the first must have size `k`, grouping is anchored from the **right (end)**.
   - The number of characters remaining for the first group is given by:
     $$\text{first\_len} = \text{len}(\text{clean}) \pmod k$$
   - If the remainder is $0$, the first group must have size $k$ (since every group has size $k$). In Python, we can write:
     ```python
     first_len = len(clean) % k or k
     ```
4. **Slice the Chunks**:
   - Add `clean[:first_len]` as the first chunk.
   - Iterate from `first_len` to the end in steps of `k` and append each chunk `clean[i : i + k]`.
5. **Join**: Return `"-".join(res)`.

### Complexity:
- **Time**: $\mathcal{O}(N)$ where $N$ is the length of `s` (linear pass to replace, slice, and join).
- **Space**: $\mathcal{O}(N)$ to store the cleaned characters and the list of chunks.

---

## Algorithm 2: Reverse Chunking (Concise & Pythonic)

### Core Idea:
Since groups of size $k$ are built from right to left, we can:
1. Strip dashes and uppercase the string: `clean = s.replace('-', '').upper()`.
2. Reverse the string: `rev = clean[::-1]`.
3. Slice into chunks of size $k$ from left to right:
   ```python
   chunks = [rev[i : i + k] for i in range(0, len(rev), k)]
   ```
4. Join the chunks with `"-"` and reverse the whole string back:
   ```python
   return "-".join(chunks)[::-1]
   ```

### Complexity:
- **Time**: $\mathcal{O}(N)$.
- **Space**: $\mathcal{O}(N)$.

---

## Pitfalls & Common Mistakes

1. **Relying on Existing Dashes**:
   - Existing dashes in `s` do not mark group boundaries. Attempting to take the substring before the first dash as the first group will fail whenever the original group sizes do not match $k$ (e.g., `s = "2-4A0r7-4k", k = 4`).
2. **`IndexError` when No Dashes Exist**:
   - Looking for `'-'` with `while s[i] != '-'` causes an out-of-bounds error if the string contains no dashes (e.g., `s = "r", k = 1`).
3. **Empty String or Only Dashes**:
   - Inputs like `s = "---"` contain 0 alphanumeric characters and should return `""`, not a string of dashes.
4. **Leading or Trailing Dashes**:
   - Inputs like `s = "--a-b-c--"` must have all surrounding dashes stripped before grouping.
