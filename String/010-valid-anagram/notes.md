# Valid Anagram

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Idea

Two strings are anagrams if and only if they have the exact same length and identical character frequencies.

Instead of creating two separate hash maps or sorting both strings, we can optimize space and runtime using a single fixed-size array of 26 integers (for lowercase English letters `a-z`):
1. **Length Check**: If `len(s) != len(t)`, they cannot be anagrams, so return `False` immediately.
2. **Frequency Cancellation**: Iterate through both strings in parallel using `zip(s, t)`. For each character pair `(a, b)`:
   - Increment the frequency slot for character `a` (from `s`).
   - Decrement the frequency slot for character `b` (from `t`).
3. **Verification**: If `s` and `t` are anagrams, every increment is balanced out by a corresponding decrement, leaving all 26 counters at `0`.

## Algorithm

1. If `len(s) != len(t)`, return `False`.
2. Initialize `count = [0] * 26` to track character frequencies.
3. Iterate through `a` and `b` in `zip(s, t)`:
   - Update `count[ord(a) - ord('a')] += 1`
   - Update `count[ord(b) - ord('a')] -= 1`
4. Return `all(x == 0 for x in count)`.

## Example

Input: `s = "anagram"`, `t = "nagaram"`

| Step | `a` (from `s`) | `b` (from `t`) | Key Count Updates |
|:---:|:---:|:---:|:---|
| 1 | `'a'` | `'n'` | `count['a'] += 1`, `count['n'] -= 1` |
| 2 | `'n'` | `'a'` | `count['n'] += 1`, `count['a'] -= 1` |
| 3 | `'a'` | `'g'` | `count['a'] += 1`, `count['g'] -= 1` |
| 4 | `'g'` | `'a'` | `count['g'] += 1`, `count['a'] -= 1` |
| 5 | `'r'` | `'r'` | `count['r'] += 1`, `count['r'] -= 1` |
| 6 | `'a'` | `'a'` | `count['a'] += 1`, `count['a'] -= 1` |
| 7 | `'m'` | `'m'` | `count['m'] += 1`, `count['m'] -= 1` |

Final `count` array: `[0, 0, 0, ..., 0]` (all 26 entries are `0`).  
Result: `True`

## Complexity

- **Time Complexity:** $O(N)$, where $N$ is the length of string `s` (or `t`). Iterating through `zip(s, t)` takes $O(N)$ time, and checking the fixed 26 elements of `count` takes $O(1)$ time.
- **Space Complexity:** $O(1)$ auxiliary space, since the `count` array fixed size is 26 regardless of input string length.

## Notes & Variations

- **Unicode Support:** If the input strings contain Unicode characters instead of just lowercase English letters, replace the fixed 26-element array with a Hash Map / `collections.Counter`.
- **Sorting Approach:** `sorted(s) == sorted(t)` takes $O(N \log N)$ time and $O(N)$ space, which is easier to write but asymptotically slower than the character counting approach.
