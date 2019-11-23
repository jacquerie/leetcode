# -*- coding: utf-8 -*-

from collections import Counter


class Solution(object):
    def domainToLevels(self, domain):
        parts = domain.split('.')

        if len(parts) == 3:
            return ['.'.join(parts[-3:]), '.'.join(parts[-2:]), parts[-1]]
        elif len(parts) == 2:
            return ['.'.join(parts[-2:]), parts[-1]]

    def subdomainVisits(self, cpdomains):
        result = Counter()

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            for level in self.domainToLevels(domain):
                result[level] += int(count)

        return ['%d %s' % (count, level) for level, count in result.items()]  # noqa: F812


if __name__ == '__main__':
    solution = Solution()

    assert sorted(['9001 discuss.leetcode.com', '9001 leetcode.com', '9001 com']) == sorted(solution.subdomainVisits(['9001 discuss.leetcode.com']))
