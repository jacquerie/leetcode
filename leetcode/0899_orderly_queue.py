# -*- coding: utf-8 -*-


class Solution:
    def orderlyQueue(self, S, K):
        if K == 1:
            return min((S + S)[i:i + len(S)] for i in range(len(S)))
        return ''.join(sorted(S))


if __name__ == '__main__':
    solution = Solution()

    assert 'acb' == solution.orderlyQueue('cba', 1)
    assert 'aaabc' == solution.orderlyQueue('baaca', 3)
