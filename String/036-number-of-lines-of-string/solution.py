class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        current_line_width = 0
        lines = 1
        for i in s:
            w = widths[ord(i)-ord("a")]
            current_line_width += w
            if current_line_width + w > 100:
                lines += 1
                current_line_width = w

        return [lines, current_line_width]