// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <stack>
#include <vector>

using namespace std;

class Solution {
 public:
  bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
    size_t i = 0, j = 0;
    stack<int> stack;

    while (i < pushed.size() || j < popped.size()) {
      if (j < popped.size() && !stack.empty() && stack.top() == popped[j]) {
        stack.pop();
        j++;
      } else if (i < pushed.size()) {
        stack.push(pushed[i]);
        i++;
      } else {
        return false;
      }
    }

    return i == pushed.size() && j == popped.size();
  }
};

int main() {
  auto solution = Solution();

  vector<int> pushed = {1, 2, 3, 4, 5};
  vector<int> popped = {4, 5, 3, 2, 1};

  assert(solution.validateStackSequences(pushed, popped));
}
