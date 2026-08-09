### Algorithm

* Start from the last digit of both binary strings.
* Add the two digits together with `carry`.
* If the sum is `2` or `3`, set `carry = 1`; otherwise set it to `0`.
* Add the resulting binary digit to the beginning of `result`.
* Continue until both strings are fully processed.
* If a carry remains, add `1` to the beginning.
* Return the result.

**Time:** `O(max(n, m))`
**Space:** `O(max(n, m))`
