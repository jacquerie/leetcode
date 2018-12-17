set -e

cpplint --recursive --quiet leetcode
flake8 leetcode
ls -1 leetcode/*.cpp | xargs --max-args 1 --max-procs 2 g++ --std=c++11
ls -1 leetcode/*.py | xargs --max-args 1 --max-procs 2 python
