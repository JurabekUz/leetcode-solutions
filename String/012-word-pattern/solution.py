class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_list = s.split(' ')

        if len(s_list) != len(pattern):
            return False

        matching_map = {}

        for i in range(len(pattern)):

            if pattern[i] in matching_map:
                if matching_map[pattern[i]] != s_list[i]:
                    return False
            elif s_list[i] in matching_map.values():
                return False

            matching_map[pattern[i]] = s_list[i]

        return True