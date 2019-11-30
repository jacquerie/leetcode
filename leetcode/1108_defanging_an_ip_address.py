# -*- coding: utf-8 -*-


class Solution:
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')


if __name__ == '__main__':
    solution = Solution()

    assert '1[.]1[.]1[.]1' == solution.defangIPaddr('1.1.1.1')
    assert '255[.]100[.]50[.]0' == solution.defangIPaddr('255.100.50.0')
