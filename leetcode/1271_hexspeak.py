# -*- coding: utf-8 -*-


class Solution:
    def toHexspeak(self, num: str) -> str:
        h = hex(int(num))[2:].replace("0", "o").replace("1", "i").upper()
        if (
            "3" in h
            or "4" in h
            or "5" in h
            or "6" in h
            or "7" in h
            or "8" in h
            or "9" in h
        ):
            return "ERROR"
        return h


if __name__ == "__main__":
    solution = Solution()

    assert "IOI" == solution.toHexspeak("257")
    assert "ERROR" == solution.toHexspeak("3")
    assert "AEIDBCDIBC" == solution.toHexspeak("747823223228")
