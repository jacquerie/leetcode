# -*- coding: utf-8 -*-


class Solution:
    def numberOfLines(self, widths, S):
        current_line_number = 1
        current_line_length = 0

        for char in S:
            char_width = widths[ord(char) - 97]
            if char_width + current_line_length <= 100:
                current_line_length += char_width
            else:
                current_line_number += 1
                current_line_length = char_width

        return [current_line_number, current_line_length]


if __name__ == '__main__':
    solution = Solution()

    assert [3, 60] == solution.numberOfLines([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 'abcdefghijklmnopqrstuvwxyz')
    assert [2, 4] == solution.numberOfLines([4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 'bbbcccdddaaa')
