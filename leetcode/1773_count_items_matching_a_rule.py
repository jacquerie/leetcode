# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return len([item for item in items if self.match(item, ruleKey, ruleValue)])

    def match(self, item: List[str], ruleKey: str, ruleValue: str) -> bool:
        type_, color, name = item
        if ruleKey == "type":
            return type_ == ruleValue
        elif ruleKey == "color":
            return color == ruleValue
        elif ruleKey == "name":
            return name == ruleValue


if __name__ == "__main__":
    solution = Solution()

    assert 1 == solution.countMatches(
        [
            ["phone", "blue", "pixel"],
            ["computer", "silver", "lenovo"],
            ["phone", "gold", "iphone"],
        ],
        "color",
        "silver",
    )
    assert 2 == solution.countMatches(
        [
            ["phone", "blue", "pixel"],
            ["computer", "silver", "phone"],
            ["phone", "gold", "iphone"],
        ],
        "type",
        "phone",
    )
