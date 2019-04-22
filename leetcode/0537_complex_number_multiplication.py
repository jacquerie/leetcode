# -*- coding: utf-8' -*-

from __future__ import absolute_import, division, print_function

import re

RE_COMPLEX_NUMBER = re.compile(r'(?P<real>-?\d+)\+(?P<imaginary>-?\d+)i')


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary,
        )

    def __str__(self):
        return '%d+%di' % (self.real, self.imaginary)

    @staticmethod
    def loads(s):
        match = RE_COMPLEX_NUMBER.match(s)
        real = int(match.group('real'))
        imaginary = int(match.group('imaginary'))

        return Complex(real, imaginary)


class Solution(object):
    def complexNumberMultiply(self, a, b):
        return str(Complex.loads(a) * Complex.loads(b))


if __name__ == '__main__':
    solution = Solution()

    assert '0+2i' == solution.complexNumberMultiply('1+1i', '1+1i')
    assert '0+-2i' == solution.complexNumberMultiply('1+-1i', '1+-1i')
