# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        doubled_code, length, result = code + code, len(code), []
        for i, _ in enumerate(code):
            if k > 0:
                result.append(sum(doubled_code[i + 1 : i + k + 1]))
            elif k < 0:
                result.append(sum(doubled_code[length + i + k : length + i]))
            else:
                result.append(0)
        return result


if __name__ == "__main__":
    solution = Solution()

    assert [12, 10, 16, 13] == solution.decrypt([5, 7, 1, 4], 3)
    assert [0, 0, 0, 0] == solution.decrypt([1, 2, 3, 4], 0)
    assert [12, 5, 6, 13] == solution.decrypt([2, 4, 9, 3], -2)
