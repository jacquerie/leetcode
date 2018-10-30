# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


def Settings(**kwargs):
    if kwargs['language'] == 'cfamily':
        return {'flags': ['-x', 'c++', '-Wall', '-Wextra', '-Werror']}
    return {}
