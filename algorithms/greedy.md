# 📌 Pattern: Greedy + Two Pointers (Assign Cookies)

### 1. Problem Overview
You are given two arrays:
* `g`: Children's greed factor (minimum cookie size each child wants).
* `s`: Cookie sizes available.

**Goal**: Maximize the number of content children. Each child gets at most one cookie, and each cookie can only be given to one child ($s[j] \ge g[i]$).

---

### 2. The Greedy Intuition
To maximize the number of satisfied children:
1. **Satisfy the least demanding child first**: A child with a smaller greed factor is easiest to make content.
2. **Use the smallest possible cookie that fits**: Never waste a large cookie on a child who would be satisfied with a small one. Save larger cookies for children with higher greed factors.

> **Key Rule**: Sorting both arrays allows us to make the locally optimal choice at every step, which guarantees the globally optimal answer.

---

### 3. Two Pointers Execution
1. Sort both `g` (greed) and `s` (cookies) in ascending order.
2. Initialize two pointers:
   * `child_i = 0` (points to the current child)
   * `cookie_j = 0` (points to the current cookie)
3. While `child_i < len(g)` and `cookie_j < len(s)`:
   * If `s[cookie_j] >= g[child_i]`: The cookie satisfies the child $\rightarrow$ advance `child_i` (child is happy).
   * Always advance `cookie_j`: Whether the cookie was used or was too small to satisfy anyone, it cannot be used for any remaining (even greedier) children.
4. The answer is simply `child_i` (the count of satisfied children).

---

### 4. Canonical Template (Python)

```python
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # Step 1: Sort both arrays to enable greedy matching
        g.sort()
        s.sort()

        child_i = 0
        cookie_j = 0

        # Step 2: Traverse using two pointers
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                # Child is satisfied, move to the next child
                child_i += 1
            # Move to the next cookie in all cases
            cookie_j += 1

        return child_i
```

---

### 5. Complexity
* **Time Complexity**: $\mathcal{O}(n \log n + m \log m)$
  * Sorting `g` of size $n$ takes $\mathcal{O}(n \log n)$ and sorting `s` of size $m$ takes $\mathcal{O}(m \log m)$.
  * Two-pointer scan takes linear time $\mathcal{O}(n + m)$.
* **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(\log n + \log m)$ depending on Python's Timsort internal stack space.

---

### 6. When to Apply This Pattern
Look for scenarios where:
* You have **two independent sets of resources and demands** (e.g., workers and tasks, boats and people, cookies and children).
* You want to **maximize matches** or **minimize wasted capacity**.
* **Canonical Problems**:
  * *LC 455*: Assign Cookies
  * *LC 881*: Boats to Save People
  * *LC 2410*: Maximum Matching of Players With Trainers
  * *LC 860*: Lemonade Change
