// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>

using namespace std;

class Solution {
 public:
  int fib(int N) {
    int current = 0, next = 1;

    for (int i = 0; i < N; i++) {
      int tmp = next;
      next = current + next;
      current = tmp;
    }

    return current;
  }
};

int main() {
  auto solution = Solution();

  assert(1 == solution.fib(2));
  assert(2 == solution.fib(3));
  assert(3 == solution.fib(4));
}
