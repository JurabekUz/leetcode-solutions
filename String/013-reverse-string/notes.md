## Pattern: Two Pointers

### Algorithm:
- Set two pointers:
  left = 0
  right = len(s) - 1
- Move toward the middle.
- Swap s[left] and s[right].
- Continue until left >= right.

Key idea:
Swap the first and last elements,
then the second and second-last,
and so on.

Why half of the length:
Each swap handles two positions,
so we only need to process half of the array.

Python:
Python allows swapping two list values in one line.