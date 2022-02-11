# -*- coding: utf-8 -*-


class Solution:
    def sortSentence(self, s: str) -> str:
        tokens = s.split()
        result = [None] * len(tokens)

        for token in tokens:
            word, index = token[:-1], int(token[-1])
            result[index - 1] = word

        return " ".join(result)


if __name__ == "__main__":
    solution = Solution()

    assert "This is a sentence" == solution.sortSentence("is2 sentence4 This1 a3")
    assert "Me Myself and I" == solution.sortSentence("Myself2 Me1 I4 and3")
