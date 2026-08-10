# Isomorphic Strings

## Problem

Given two strings `s` and `t`, determine if they are isomorphic. Two strings are isomorphic if the characters in `s` can be mapped to characters in `t` such that the character order is preserved, and no two characters in `s` map to the same character in `t`.

## Idea

To determine if two strings are isomorphic, we must establish a one-to-one (bijection) character mapping between `s` and `t`. As we iterate through both strings simultaneously:
1. If character `s[i]` has already been mapped, check whether it maps to `t[i]`. If not, return `False`.
2. If `s[i]` is not mapped yet, but `t[i]` is already mapped from another character in `s` (`t[i] in matching.values()`), return `False` to prevent multiple characters from mapping to the same target character.
3. Otherwise, record the mapping `matching[s[i]] = t[i]`.

## Algorithm

1. Create an empty dictionary `matching` to store character mappings from `s` to `t`.
2. Loop through indices `i` from `0` to `len(s) - 1`:
   - If `s[i]` is in `matching`:
     - If `matching[s[i]] != t[i]`, return `False`.
   - Else if `t[i]` is already mapped (`t[i] in matching.values()`):
     - Return `False`.
   - Else:
     - Set `matching[s[i]] = t[i]`.
3. If all characters pass validation, return `True`.

## Example

Input: `s = "egg"`, `t = "add"`

| Index `i` | `s[i]` | `t[i]` | `matching` | Action / Result |
|---|---|---|---|---|
| 0 | `e` | `a` | `{'e': 'a'}` | New mapping created |
| 1 | `g` | `d` | `{'e': 'a', 'g': 'd'}` | New mapping created |
| 2 | `g` | `d` | `{'e': 'a', 'g': 'd'}` | `matching['g'] == 'd'`, Valid |

Result: `True`

## Complexity

- Time: $O(N \cdot K)$ where $N$ is string length and $K$ is unique characters (due to linear lookup in `matching.values()`). Using two maps or a set of mapped values brings this to $O(N)$.
- Space: $O(K)$ where $K$ is the number of unique character mappings in the dictionary.

## Notes

- **Edge Cases:** Single character strings are always isomorphic.
- **Alternative Approaches:** Using two dictionaries (`s_to_t` and `t_to_s`) or checking character last-seen positions (`s.find(char) == t.find(char)`) eliminates the $O(K)$ lookup in values.
- **What You Learned:** A valid isomorphic mapping requires checking both directions to guarantee a one-to-one (bijective) correspondence.
