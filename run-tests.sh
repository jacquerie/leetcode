# -*- coding: utf-8 -*-

set -e

cpplint --recursive --quiet leetcode
flake8 leetcode
