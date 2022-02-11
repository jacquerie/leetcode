# -*- coding: utf-8 -*-


class Solution:
    def reorderSpaces(self, text: str) -> str:
        number_of_spaces = text.count(" ")
        words = text.split()

        if len(words) == 1:
            return words[0] + " " * number_of_spaces
        between_words, at_the_end = divmod(number_of_spaces, len(words) - 1)
        return (" " * between_words).join(words) + " " * at_the_end


if __name__ == "__main__":
    solution = Solution()

    assert "this   is   a   sentence" == solution.reorderSpaces(
        "  this   is  a sentence "
    )
    assert "practice   makes   perfect " == solution.reorderSpaces(
        " practice   makes   perfect"
    )
    assert "hello   world" == solution.reorderSpaces("hello   world")
    assert "walks  udp  package  into  bar  a " == solution.reorderSpaces(
        "  walks  udp package   into  bar a"
    )
    assert "a" == solution.reorderSpaces("a")
