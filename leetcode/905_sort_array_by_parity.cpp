// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int i = 0, j = A.size() - 1;
        while (i < j) {
            if (A[i] % 2 == 0) {
                i++;
            } else if (A[j] % 2 == 1) {
                j--;
            } else {
                swap(A[i++], A[j--]);
            }
        }

        return A;
    }
};

int main() {
    auto solution = Solution();

    vector<int> A = {3, 1, 2, 4};

    vector<int> expected = {4, 2, 1, 3};
    vector<int> result = solution.sortArrayByParity(A);

    assert(expected == result);
}
