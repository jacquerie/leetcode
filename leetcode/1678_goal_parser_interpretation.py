# -*- coding: utf-8 -*-


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


if __name__ == "__main__":
    solution = Solution()

    assert "Goal" == solution.interpret("G()(al)")
    assert "Gooooal" == solution.interpret("G()()()()(al)")
    assert "alGalooG" == solution.interpret("(al)G(al)()()G")
