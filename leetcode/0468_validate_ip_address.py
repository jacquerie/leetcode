# -*- coding: utf-8 -*-

import socket


class Solution(object):
    def validIPv4Address(self, IP):
        try:
            socket.inet_pton(socket.AF_INET, IP)
        except socket.error:
            return False
        return True

    def validIPv6Address(self, IP):
        if '::' in IP:
            return False

        if any(len(group) > 4 and group.startswith('0') for group in IP.split(':')):
            return False

        try:
            socket.inet_pton(socket.AF_INET6, IP)
        except socket.error:
            return False
        return True

    def validIPAddress(self, IP):
        if self.validIPv4Address(IP):
            return 'IPv4'
        elif self.validIPv6Address(IP):
            return 'IPv6'
        return 'Neither'


if __name__ == '__main__':
    solution = Solution()

    assert 'IPv4' == solution.validIPAddress('172.16.254.1')
    assert 'IPv6' == solution.validIPAddress('2001:0db8:85a3:0:0:8A2E:0370:7334')
    assert 'IPv6' == solution.validIPAddress('2001:db8:85a3:0:0:8A2E:0370:7334')
    assert 'Neither' == solution.validIPAddress('2001:0db8:85a3::8A2E:0370:7334')
    assert 'Neither' == solution.validIPAddress('02001:0db8:85a3:0000:0000:8a2e:0370:7334')
    assert 'Neither' == solution.validIPAddress('256.256.256.256')
