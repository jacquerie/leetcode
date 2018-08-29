# -*- coding: utf-8 -*-

set -e

cpplint --recursive --quiet leetcode
flake8 leetcode
ls -1 leetcode/*.py | xargs --max-args 1 --max-procs 2 python
