class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)

        while left < right:
            while left < right and s[left].lower() not in vowels:
                left += 1

            while left < right and s[right].lower() not in vowels:
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)



