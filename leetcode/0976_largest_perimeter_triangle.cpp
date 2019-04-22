// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <functional>
#include <vector>

using namespace std;

class Solution {
 public:
  int largestPerimeter(vector<int>& A) {
    sort(A.begin(), A.end(), greater<int>());

    for (int i = 0; i < A.size() - 2; i++) {
      if (A[i + 2] + A[i + 1] > A[i]) {
        return A[i + 2] + A[i + 1] + A[i];
      }
    }

    return 0;
  }
};

int main() {
  auto solution = Solution();

  vector<int> A = {2, 1, 2};

  assert(5 == solution.largestPerimeter(A));
}
