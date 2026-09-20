class Solution:
    def backspaceCompare(s: str, t: str) -> bool:
        def build(st: str) -> list:
            stack = []
            for ch in st:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return stack

        return build(s) == build(t)