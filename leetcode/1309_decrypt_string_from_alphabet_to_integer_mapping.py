# -*- coding: utf-8 -*-


class Solution:
    INTEGER_TO_ALPHABET = {n: chr(ord("a") + n - 1) for n in range(1, 27)}

    def freqAlphabets(self, s: str) -> str:
        i, result = 0, []
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                result.append(self.INTEGER_TO_ALPHABET[int(s[i : i + 2])])
                i += 3
            else:
                result.append(self.INTEGER_TO_ALPHABET[int(s[i : i + 1])])
                i += 1
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    assert "jkab" == solution.freqAlphabets("10#11#12")
    assert "acz" == solution.freqAlphabets("1326#")
    assert "y" == solution.freqAlphabets("25#")
    assert "abcdefghijklmnopqrstuvwxyz" == solution.freqAlphabets(
        "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    )
