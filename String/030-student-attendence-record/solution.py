class Solution:
    def checkRecord(self, s: str) -> bool:

        count_l = 0
        l = False
        count_a = 0
        for i in s:
            if i == 'A':
                l = False
                count_a += 1
            elif i == "L":
                count_l = count_l + 1 if l else 1
                l = True
            else:
                l = False

            if count_l == 3 or count_a == 2:
                return False

        return True

# this function can be optimized by redundant or using builtin features


