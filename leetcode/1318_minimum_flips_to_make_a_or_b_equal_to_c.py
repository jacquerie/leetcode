# -*- coding: utf-8 -*-


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0

        a_str, b_str, c_str = format(a, '032b'), format(b, '032b'), format(c, '032b')
        for a_chr, b_chr, c_chr in zip(a_str, b_str, c_str):
            a_int, b_int, c_int = int(a_chr), int(b_chr), int(c_chr)
            if a_int | b_int != c_int:
                result += 2 if a_int == 1 and b_int == 1 else 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.minFlips(2, 6, 5)
    assert 1 == solution.minFlips(4, 2, 7)
    assert 0 == solution.minFlips(1, 2, 3)
