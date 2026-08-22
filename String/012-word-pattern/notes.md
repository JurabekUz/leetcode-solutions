### pattern: Bidirectional Mapping / Bijection.


### Algorithm

1. Split s into words.
2. If number of letters != number of words:
   return false.

3. Create two maps:
   letter → word
   word → letter

4. For each letter and word:

   If letter already maps to another word:
       return false

   If word already maps to another letter:
       return false

   Otherwise:
       create both mappings

5. If every pair is valid:
   return true
