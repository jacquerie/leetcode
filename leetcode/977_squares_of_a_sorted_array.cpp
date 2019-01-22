// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> sortedSquares(vector<int>& A) {
    vector<int> result;

    int i = 0, j = A.size() - 1;
    while (i <= j) {
      if (abs(A[i]) < abs(A[j])) {
        result.push_back(A[j] * A[j]);
        j--;
      } else {
        result.push_back(A[i] * A[i]);
        i++;
      }
    }

    reverse(result.begin(), result.end());

    return result;
  }
};

int main() {
  auto solution = Solution();

  vector<int> A = {-4, -1, 0, 3, 10};

  vector<int> expected = {0, 1, 9, 16, 100};
  vector<int> result = solution.sortedSquares(A);

  assert(expected == result);
}
