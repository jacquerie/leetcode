// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> diStringMatch(string S) {
    vector<int> result = {0};

    int max = 0, min = 0;
    for (const auto& c : S) {
      if (c == 'I') {
        result.push_back(++max);
      } else {
        result.push_back(--min);
      }
    }

    for (size_t i = 0; i < result.size(); i++) {
      result[i] -= min;
    }

    return result;
  }
};

int main() {
  auto solution = Solution();

  vector<int> expected = {2, 3, 1, 4, 0};
  vector<int> result = solution.diStringMatch("IDID");

  assert(expected == result);
}
