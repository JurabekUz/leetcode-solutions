# Approach

## Idea

A valid parentheses string must satisfy two conditions:

1. Every opening bracket must be closed by the correct type of closing bracket.
2. Brackets must be closed in the correct order.

To keep track of unmatched opening brackets, I use a **stack**. Whenever I encounter an opening bracket, I push it onto the stack. When I encounter a closing bracket, I check whether it matches the most recent opening bracket. If it does, I remove the opening bracket from the stack. Otherwise, the string is invalid.

After processing the entire string, the stack should be empty. If it is not, there are unmatched opening brackets remaining.

## Algorithm

1. Create a dictionary that maps each opening bracket to its corresponding closing bracket.
2. Initialize an empty stack.
3. Iterate through each character in the string.
4. If the character is an opening bracket, push it onto the stack.
5. Otherwise, it is a closing bracket:
   - If the stack is empty, return `False`.
   - Check whether the closing bracket matches the opening bracket at the top of the stack.
   - If it does not match, return `False`.
   - Otherwise, pop the opening bracket from the stack.
6. After processing all characters, return `True` if the stack is empty; otherwise, return `False`.

## Example

Input:

```text
({[]})
```

| Character | Stack | Action |
|-----------|-------|--------|
| `(` | `(` | Push |
| `{` | `({` | Push |
| `[` | `({[` | Push |
| `]` | `({` | Pop |
| `}` | `(` | Pop |
| `)` | Empty | Pop |

Result: `True`

## Complexity

- **Time:** `O(n)` — each character is processed once.
- **Space:** `O(n)` — in the worst case, all opening brackets are stored in the stack.