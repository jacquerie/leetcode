// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
 public:
  int repeatedNTimes(vector<int>& A) {
    unordered_set<int> seen;
    for (const auto& el : A) {
      if (seen.find(el) != seen.end()) {
        return el;
      }

      seen.insert(el);
    }
  }
};

int main() {
  auto solution = Solution();

  vector<int> A = {1, 2, 3, 3};

  assert(3 == solution.repeatedNTimes(A));
}
