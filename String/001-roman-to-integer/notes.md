# Approach

## Idea

Roman numerals are usually added together from left to right. However, when a smaller numeral appears before a larger one (such as `IV` or `IX`), it represents subtraction instead of addition.

Instead of deciding whether to add or subtract immediately, I keep a list of processed values. If I later discover that the current numeral is larger than the previous one, I replace the previous value with the difference. Otherwise, I simply store the current value. Finally, I sum all processed values.

## Algorithm

1. Create a dictionary that maps each Roman numeral to its integer value.
2. Add the value of the first character to a list.
3. Traverse the remaining characters from left to right.
4. For each character:
   - If its value is greater than the last value stored in the list, replace the last value with the difference between the current and previous values.
   - Otherwise, append the current value to the list.
5. Return the sum of all values in the list.

## Example

Input: `MCMIV`

| Character | Processed List |
|-----------|----------------|
| M (1000) | [1000] |
| C (100) | [1000, 100] |
| M (1000) | [1000, 900] |
| I (1) | [1000, 900, 1] |
| V (5) | [1000, 900, 4] |

Result = `1000 + 900 + 4 = 1904`

## Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`