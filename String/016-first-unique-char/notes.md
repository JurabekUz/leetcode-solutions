Pattern:
Frequency Counter + Ordered Scan

Algorithm:

1. Count the frequency of every character.
2. Scan the string from left to right.
3. For each character:
       if its frequency == 1:
           return its index
4. If no character has frequency 1:
       return -1