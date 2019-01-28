set -e

cpplint --recursive --quiet leetcode
ktlint leetcode/*.kt
flake8 leetcode

ls -1 leetcode/*.cpp | xargs --max-args 1 --max-procs 1 -I % sh -c 'g++ --std=c++11 -Wall -Wextra -Werror -Wno-return-type -Wno-sign-compare -Wno-unused-but-set-variable %; ./a.out;'
ls -1 leetcode/*.py | xargs --max-args 1 --max-procs 2 python
