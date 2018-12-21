# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


def Settings(**kwargs):
    if kwargs['language'] == 'cfamily':
        return {
            'flags': [
                '--std=c++11',
                '-Wall',
                '-Wextra',
                '-Werror',
                '-Wno-return-type',
                '-Wno-sign-compare',
                '-Wno-unused-but-set-variable',
            ],
        }
    return {}
