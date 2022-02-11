# -*- coding: utf-8 -*-

import itertools


class Solution:
    def isLongPressedName(self, name, typed):
        for name_group, typed_group in itertools.zip_longest(
            itertools.groupby(name), itertools.groupby(typed)
        ):
            if name_group is None or typed_group is None:
                return False
            elif name_group[0] != typed_group[0]:
                return False
            elif len(list(name_group[1])) > len(list(typed_group[1])):
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.isLongPressedName("alex", "aaleex")
    assert not solution.isLongPressedName("saeed", "ssaaedd")
    assert solution.isLongPressedName("leelee", "lleeelee")
    assert solution.isLongPressedName("laiden", "laiden")
