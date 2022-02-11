# -*- coding: utf-8 -*-


class Solution:
    def reformatNumber(self, number: str) -> str:
        cleaned_number = number.replace("-", "").replace(" ", "")
        if len(cleaned_number) % 3 == 0:
            prefix, suffix = cleaned_number, ""
        elif len(cleaned_number) % 3 == 1:
            prefix, suffix = cleaned_number[:-4], cleaned_number[-4:]
        elif len(cleaned_number) % 3 == 2:
            prefix, suffix = cleaned_number[:-2], cleaned_number[-2:]

        return "-".join(
            [prefix[i : i + 3] for i in range(0, len(prefix), 3)]
            + [suffix[i : i + 2] for i in range(0, len(suffix), 2)]
        )


if __name__ == "__main__":
    solution = Solution()

    assert "123-456" == solution.reformatNumber("1-23-45 6")
    assert "123-45-67" == solution.reformatNumber("123 4-567")
    assert "123-456-78" == solution.reformatNumber("123 4-5678")
    assert "12" == solution.reformatNumber("12")
    assert "175-229-353-94-75" == solution.reformatNumber("--17-5 229 35-39475 ")
