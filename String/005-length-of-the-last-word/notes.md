**Algorithm (Two-Pointer / Reverse Traversal)**

1. Start from the **last character** of the string.
2. Skip all **trailing spaces** by moving the pointer to the left until a non-space character is found.
3. Initialize a counter `length = 0`.
4. Continue moving the pointer to the left while the current character is **not a space**:

   * Increment `length`.
   * Move the pointer one position to the left.
5. Stop when you reach the beginning of the string or encounter a space.
6. Return `length`.

**Time Complexity:** `O(n)`, where `n` is the length of the string. In the worst case, every character is visited once.

**Space Complexity:** `O(1)`, since only a few variables are used regardless of the input size.
