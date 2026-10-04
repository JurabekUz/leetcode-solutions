# 📌 Pattern: Value-to-Index Mapping (In-Place Negation)

### 1. The Core Intuition
Whenever a problem gives you an array of size $n$ with numbers strictly in the range:
$$\mathbf{1 \le nums[i] \le n}$$

You **do not need a `HashSet`** or extra memory. The array itself can serve as its own hash table because every valid number maps to a valid 0-based array index:

$$\mathbf{index = |value| - 1}$$

```text
Value:  1  2  3  4  5  ...  n
Index:  0  1  2  3  4  ...  n-1
```

---

### 2. The Negation Technique
Instead of storing extra flags, we use the **sign of `nums[index]`** to represent state:
* **Positive value (`nums[index] > 0`)**: The number `index + 1` has **not** been seen yet.
* **Negative value (`nums[index] < 0`)**: The number `index + 1` **exists** in the array.

#### Why two key rules matter:
1. **Always read with `abs(n)`**: The current value might have already been turned negative by an earlier iteration.
2. **Mark using `-abs(nums[index])`**: Avoid multiplying by `-1` directly; using `-abs()` ensures duplicates do not accidentally flip the flag back to positive.

---

### 3. Canonical Template (Python)

```python
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Step 1: Mark visited indices as negative
        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])

        # Step 2: Positive indices correspond to missing numbers
        return [i + 1 for i, val in enumerate(nums) if val > 0]
```

---

### 4. Complexity
* **Time Complexity**: $\mathcal{O}(n)$ — Two linear passes over the array.
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary space — Modifies the array in-place.

---

### 5. When to Apply This Pattern
Look for these problem keywords / constraints:
* Array size is $n$, and elements are bounded in $[1, n]$ (or $[0, n-1]$).
* Follow-up requirement: **$\mathcal{O}(n)$ time and $\mathcal{O}(1)$ extra space**.
* **Common Problems**:
  * *LC 448*: Find All Numbers Disappeared in an Array
  * *LC 442*: Find All Duplicates in an Array
  * *LC 41*: First Missing Positive
  * *LC 287*: Find the Duplicate Number
