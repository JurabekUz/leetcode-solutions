## Pattern: Two Pointers

### Recognition:
Need to reverse only specific elements (vowels)
while keeping all other elements in their original positions.

### Algorithm:

 - left  → start of string
 - right → end of string

While left < right:

    Move left until it points to a vowel.
    Move right until it points to a vowel.

    Swap the two vowels.

    Move both pointers inward.