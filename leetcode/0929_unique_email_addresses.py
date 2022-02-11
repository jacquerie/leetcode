# -*- coding: utf-8 -*-

from collections import namedtuple

Email = namedtuple("Email", ["local_name", "domain_name"])


class Solution:
    def numUniqueEmails(self, emails):
        result = set()
        for email in emails:
            raw_local_name, domain_name = email.split("@")
            local_name = raw_local_name.replace(".", "").split("+")[0]
            result.add(Email(local_name, domain_name))
        return len(result)


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.numUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
    )
