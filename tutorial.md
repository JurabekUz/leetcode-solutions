# Subsequence Pattern & Two-Pointer Insights

## 1. Why Frequency Counting / ASCII Check Fails for Subsequences
- **Key Insight**: Frequency counting (e.g. `Counter`, hash map) and ASCII sum checks do **not** work for subsequence problems because a subsequence requires the **relative order** of characters to be strictly preserved.
- **Example**:
  - `s = "axc"`, `t = "ahbgdc"`
  - All individual characters `'a'`, `'x'`, `'c'` exist in `t`, so frequency counting would report a match.
  - However, `'x'` does not appear *after* `'a'` in `t`. Therefore, `s` is **not** a valid subsequence (`False`).

---

## 2. The Two-Pointer Pattern (Optimal Solution)
- **Why it works**: Two pointers allow you to check order in a single forward pass without re-checking or backtracking.
  - Pointer `j` traverses the main text string `t` sequentially.
  - Pointer `i` only advances when a match `s[i] == t[j]` is found.
- **Complexity**:
  - **Time Complexity**: $\mathcal{O}(n)$ (where $n = \text{len}(t)$)
  - **Space Complexity**: $\mathcal{O}(1)$ (uses only two scalar integer pointers)

---

## 3. String Slicing / Mutation Pitfall
- **Avoid Slicing**: Do not actually slice or remove characters from strings (e.g., `t = t[1:]`).
- **Performance Impact**:
  - Slicing strings in Python creates a new copy of the string in memory each time.
  - Doing this inside a loop degrades performance to **$\mathcal{O}(n^2)$ time** and **$\mathcal{O}(n)$ space**.
- **Best Practice**: Use index pointer variables (`i`, `j`) to advance positions instead of modifying the string.

---

# Essential Mathematical Formulas & Branchless Arithmetic in DSA

In algorithm design, avoiding conditional branches (`if/else`) with direct mathematical and arithmetic formulas is known as **Branchless Arithmetic** (or **Condition-Free Math**). It simplifies code, eliminates branching overhead, and produces elegant one-liners.

---

## 1. Largest Multiple $\le n$ (Floor to Multiple / Discard Remainder)

### Formula:
$$\text{Largest multiple of } k \le n = \lfloor n / k \rfloor \times k = n - (n \pmod k)$$
In Python: `(n // k) * k` or `n - (n % k)`

### Special Case: Largest Even Number $\le n$ ($k = 2$)
* **Arithmetic**: `(count // 2) * 2` or `count - (count % 2)`
* **Bitwise**: `count & ~1` (clears the lowest bit)
* **Application**: 
  - **LeetCode 409 (Longest Palindrome)**: Each character with count $c$ can contribute at most `(c // 2) * 2` characters to symmetric palindrome pairs.

---

## 2. Ceiling Division (Rounding UP without `math.ceil`)

### Formula:
$$\lceil n / k \rceil = \lfloor (n + k - 1) / k \rfloor$$
In Python: `(n + k - 1) // k`

### Why it works:
Adding $k - 1$ ensures that any fractional remainder $\ge 1/k$ pushes the numerator into the next multiple of $k$, while exact multiples of $k$ remain unchanged.

### Application:
* **Batching / Pagination**: If you have $n = 10$ items and page size $k = 3$, pages needed = `(10 + 3 - 1) // 3 = 12 // 3 = 4`.
* **LeetCode 875 (Koko Eating Bananas)**: Time required to eat pile of size `p` at speed `k` is `(p + k - 1) // k`.

---

## 3. Cyclic Wrap-Around (Circular Arrays & Buffers)

### Formulas:
* **Forward step**: `(index + step) % n`
* **Backward step**: `(index - step + n) % n` (adding `+ n` prevents negative modulo in C++/Java)

### Application:
* Circular Queues, rotating arrays, clock arithmetic, round-robin scheduling.

---

## 4. 2D Grid $\longleftrightarrow$ 1D Array Coordinate Mapping

Treating a 2D matrix of shape `ROWS x COLS` as a flat 1D array of size `ROWS * COLS`:

| Conversion | Formula | Python Code |
| :--- | :--- | :--- |
| **2D $\to$ 1D Index** | $\text{index} = r \times \text{COLS} + c$ | `index = r * cols + c` |
| **1D $\to$ 2D Row** | $r = \lfloor \text{index} / \text{COLS} \rfloor$ | `r = index // cols` |
| **1D $\to$ 2D Col** | $c = \text{index} \pmod{\text{COLS}}$ | `c = index % cols` |

### Application:
* **LeetCode 74 (Search a 2D Matrix)**: Run standard binary search on `0 .. (rows * cols - 1)` and map `mid` back to `(mid // cols, mid % cols)`.

---

## 5. Parity & Boolean Indicators as Numbers

### Formulas:
* **Parity (Odd/Even check)**: `n % 2` or `n & 1` ($0 \to \text{even}$, $1 \to \text{odd}$).
* **Boolean Indicator in Arithmetic**: Convert a boolean condition directly to $0$ or $1$ (`int(cond)` or `bool(x)`).

### Application:
* **LeetCode 409 (Longest Palindrome - Odd Count Method)**:
  ```python
  odds = sum(v % 2 for v in Counter(s).values())
  return len(s) - odds + int(odds > 0)
  ```
  *(Subtract all odd remainders, and add back 1 if there was at least one odd character for the center).*

---

## 6. Bitwise XOR Self-Cancellation

### Formula:
$$x \oplus x = 0 \quad \text{and} \quad x \oplus 0 = x$$

### Application:
* Finding the unique non-duplicate element (LeetCode 136: Single Number).
* Finding the added character between two strings (LeetCode 389: Find the Difference).
