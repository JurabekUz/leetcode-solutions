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

## 4. String Prepending Pitfall ($\mathcal{O}(n^2)$ vs $\mathcal{O}(n)$ List Append)
- **Avoid Repeated Prepending**: Avoid constructing strings by prepending inside loops (e.g., `res = str(digit) + res`).
- **Performance Impact**:
  - Strings in Python are immutable. Prepending a character or substring creates a new string object and copies all previous characters in memory on every iteration.
  - Repeating this for a string of length $n$ requires:
    $$1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2} = \mathcal{O}(n^2) \text{ operations}$$
- **Optimal Pattern (Append & Reverse)**:
  - Append digits to a list: `res.append(str(digit))` ($\mathcal{O}(1)$ amortized per operation).
  - Reverse and join at the end: `''.join(reversed(res))` ($\mathcal{O}(n)$ time total).
- **Application**:
  - **LeetCode 415 (Add Strings)**, **LeetCode 67 (Add Binary)**, **LeetCode 2 (Add Two Numbers)**.

---

## 5. String Periodicity & The Doubling Trick Pitfall
- **Core Concept**: Checking if string $s$ can be constructed by repeating a smaller substring.
- **Gotchas**:
  1. **The Doubling Trick Boundary Gotcha (`[1:-1]`)**:
     - `s in (s + s)` is **always True** for any string because $s$ is trivially present at index $0$ and index $n$.
     - You **must** slice off the first and last characters: `s in (s + s)[1:-1]`.
     - Dropping index $0$ destroys the first trivial instance of $s$, and dropping the last index destroys the second instance. If $s$ still exists in the remaining string, it proves $s$ has internal periodic symmetry.
  2. **Divisibility Filter Gotcha**:
     - When scanning candidate prefix lengths $l$, always guard with `if len(s) % l == 0:`.
     - Non-divisors can never tile $s$ without a remainder. Skipping them reduces checks from $n / 2$ to at most $d(n) \le 64$ for $n \le 10^4$.
  3. **Upper Bound Gotcha**:
     - Candidate prefix lengths only need to run up to `len(s) // 2`. A repeating substring must appear at least twice, so its length cannot exceed half the string.
- **Application**:
  - **LeetCode 459 (Repeated Substring Pattern)**.

---

## 6. Membership Testing Pitfall: String Scan ($\mathcal{O}(L)$) vs. Set Lookup ($\mathcal{O}(1)$)
- **Core Concept**:
  - Checking `element in string` (or `element in list`) performs an **$\mathcal{O}(L)$ linear scan** through the sequence of length $L$.
  - In contrast, checking `element in set` (or `element in dict`) is a hash table lookup taking **$\mathcal{O}(1)$ time on average**.
- **Performance Impact**:
  - Checking whether $M$ characters of a word belong to a string of length $L$ takes $\mathcal{O}(M \times L)$.
  - Doing this across $N$ words takes $\mathcal{O}(N \times M \times L)$.
  - Pre-converting the target characters into a `set` drops membership checks to $\mathcal{O}(1)$ per character, reducing total time to $\mathcal{O}(N \times M)$.
- **Set Subset Pattern (`<=` or `.issubset()`)**:
  - When checking whether all characters of a word belong to an allowed collection:
    ```python
    # Instead of manual loops and O(L) string scans:
    # for char in word: if char not in string_collection: ...

    # Predefine allowed characters as a set:
    allowed = set("qwertyuiop")

    # Use set subset operator (O(M) to construct set, O(M) to check subset):
    if set(word.lower()) <= allowed:
        res.append(word)
    ```
- **Application**:
  - **LeetCode 500 (Keyboard Row)**: Validating words against keyboard rows (`set("qwertyuiop")`).
  - **LeetCode 345 (Reverse Vowels of a String)**: Testing vowel membership (`if char in set("aeiouAEIOU")`).

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

---

## 7. Character & Digit Conversion via ASCII Offsets

### Formulas:
* **Character to Digit**: `ord(c) - ord('0')` (or `ord(c) - 48`)
* **Digit to Character**: `chr(digit + ord('0'))` (or `chr(digit + 48)`)
* **Alphabet Index (0–25)**:
  - Lowercase: `ord(c) - ord('a')`
  - Uppercase: `ord(c) - ord('A')`
* **Index to Alphabet**: `chr(index + ord('a'))`

### Why it works:
In ASCII and Unicode standards, numeric digits (`'0'` through `'9'`) and English alphabetic characters are contiguous:
- `'0'` has code point $48$, `'9'` has code point $57$.
- Subtracting `ord('0')` directly yields the numerical digit ($0$ through $9$) without relying on `int()` or dictionary lookups.

### Application:
* **LeetCode 415 (Add Strings) / LeetCode 43 (Multiply Strings)**: Converting digit characters to integer values when direct type conversion (`int()`) is forbidden.
* **LeetCode 8 (String to Integer - atoi)**: Building integers character-by-character: `num = num * 10 + (ord(c) - ord('0'))`.
* **Fixed-size Frequency Buckets**: Using `count = [0] * 26` with `count[ord(c) - ord('a')] += 1` instead of a hash table for $\mathcal{O}(1)$ space, zero hash collisions, and fast CPU cache locality.

---

## 8. Infinity Sentinel Values (`float('inf')` & `float('-inf')`)

### Concept:
* **`float('inf')` ($+\infty$)**: Positive infinity. Har qanday son undan kichik (`x < float('inf')` $\to$ `True`).
* **`float('-inf')` ($-\infty$)**: Negative infinity. Har qanday son undan katta (`x > float('-inf')` $\to$ `True`).

### Nega `None` yoki ixtiyoriy katta son emas?
1. **To‘g‘ridan-to‘g‘ri taqqoslash**: `x < None` xatolik (`TypeError`) beradi, `float('inf')` esa bermaydi. Shuning uchun ortiqcha `if min_val is None:` tekshiruvi shart emas.
2. **Xavfsizlik**: `999999` kabi "sehrli sonlar" kiritilgan qiymat undan oshib ketsa xato beradi, cheksizlik esa yo‘q.

### Qo‘llanilishi:
```python
# Minimum topish (boshlang'ich: +inf)
min_val = float('inf')
for x in nums:
    if x < min_val:
        min_val = x

# Maximum topish (boshlang'ich: -inf)
max_val = float('-inf')
for x in nums:
    if x > max_val:
        max_val = x
```
* **Application**: LeetCode 599 (Minimum Index Sum of Two Lists), Dijkstra, DP base cases.

