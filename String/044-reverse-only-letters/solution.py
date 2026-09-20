class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        s_list = list(s)
        while j > i:
            if s_list[i].isalpha() and s_list[j].isalpha():
                s_list[j], s_list[i] = s_list[i], s_list[j]
                j -= 1
                i += 1
            else:
                if not s_list[i].isalpha():
                    i += 1

                if not s_list[j].isalpha():
                    j -= 1

        return ''.join(s_list)
