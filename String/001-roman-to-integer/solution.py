class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = [values[s[0]]]

        for char in s[1:]:
            current = values[char]

            if result[-1] < current:
                result[-1] = current - result[-1]
            else:
                result.append(current)

        return sum(result)