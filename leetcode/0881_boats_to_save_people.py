# -*- coding: utf-8 -*-


class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()

        result = 0

        i, j = 0, len(people) - 1
        while i <= j:
            result += 1
            if i == j:
                break
            elif people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.numRescueBoats([1, 2], 3)
    assert 3 == solution.numRescueBoats([3, 2, 2, 1], 3)
    assert 4 == solution.numRescueBoats([3, 5, 3, 4], 5)
