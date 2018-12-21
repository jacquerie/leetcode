set -e

cpplint --recursive --quiet leetcode
flake8 leetcode
ls -1 leetcode/*.cpp | xargs --max-args 1 --max-procs 2 g++ --std=c++11 -Wall -Wextra -Werror -Wno-return-type -Wno-sign-compare -Wno-unused-but-set-variable
ls -1 leetcode/*.py | xargs --max-args 1 --max-procs 2 python
